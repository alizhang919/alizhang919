import csv
from paper_plot_style import plt, OI, save_fig
rows = list(csv.DictReader(open('table41.csv')))
classes = list(dict.fromkeys(r['class'] for r in rows))
readings = list(dict.fromkeys(r['reading'] for r in rows))
colors = [OI['blue'], OI['orange'], OI['grey']]
markers = ['o', 's', 'D']
fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.6), sharey=True)
for ax, cls in zip(axes, classes):
    sub = [r for r in rows if r['class'] == cls]
    for i, r in enumerate(sub):
        y = len(sub) - 1 - i
        m, lo, hi = float(r['mean']), float(r['ci_lo']), float(r['ci_hi'])
        ax.plot([lo, hi], [y, y], color=colors[i], lw=1.6)
        ax.plot(m, y, marker=markers[i], color=colors[i], ms=5, ls='none')
        ax.text(hi + 6, y, f"G={r['G']}, p={float(r['p_signflip']):.3f}", va='center', fontsize=7)
    ax.axvline(0, color='black', lw=0.7, ls='--')
    ax.set_xlabel('Equal-pair mean differential (bp)')
    ax.text(0.0, 1.04, cls, transform=ax.transAxes, fontsize=9, fontweight='bold')
    lo_all = min(float(r['ci_lo']) for r in sub); hi_all = max(float(r['ci_hi']) for r in sub)
    ax.set_xlim(lo_all - 15, hi_all + 95)
axes[0].set_yticks([2, 1, 0])
axes[0].set_yticklabels(['Final\n(full horizon)', 'Pre-specified\nwindow', 'Benchmark\n(original pairs)'])
fig.tight_layout(w_pad=1.0)
save_fig(fig, 'figA_estimates_by_reading')
