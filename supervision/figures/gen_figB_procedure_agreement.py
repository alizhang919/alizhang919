import csv
from paper_plot_style import plt, OI, save_fig
rows = list(csv.DictReader(open('procedures.csv')))
specs = list(dict.fromkeys(r['specification'] for r in rows))
procs = list(dict.fromkeys(r['procedure'] for r in rows))
fig, ax = plt.subplots(figsize=(5.2, 2.7))
cols = [OI['blue'], OI['verm']]
h = 0.36
for j, s in enumerate(specs):
    for i, p in enumerate(procs):
        val = float(next(r['p'] for r in rows if r['specification'] == s and r['procedure'] == p))
        y = i + (j - 0.5) * h
        ax.barh(y, val, height=h * 0.9, color=cols[j], label=s if i == 0 else None)
        ax.text(val * 1.12, y, f'{val:.3f}', va='center', fontsize=7, bbox=dict(facecolor='white', edgecolor='none', pad=0.5))
ax.axvline(0.05, color='black', lw=0.8, ls='--')
ax.text(0.052, -0.62, 'p = 0.05', fontsize=7, va='center')
ax.set_xscale('log'); ax.set_xlim(0.005, 1.5)
from matplotlib.ticker import FixedLocator, FixedFormatter
ax.xaxis.set_major_locator(FixedLocator([0.01,0.05,0.1,0.5,1])); ax.xaxis.set_major_formatter(FixedFormatter(['0.01','0.05','0.10','0.50','1.00'])); ax.xaxis.set_minor_formatter(FixedFormatter([]))
ax.set_ylim(len(procs)-0.4, -0.8)
ax.set_yticks(range(len(procs))); ax.set_yticklabels(procs)
ax.set_xlabel('Unadjusted two-sided p-value (log scale)')
ax.legend(frameon=False, loc='lower center', bbox_to_anchor=(0.45, 1.0), ncol=1, fontsize=7)
save_fig(fig, 'figB_procedure_agreement')
