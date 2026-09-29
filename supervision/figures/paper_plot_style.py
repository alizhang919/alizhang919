import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({
    'font.size': 9, 'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'Times New Roman', 'DejaVu Serif'],
    'axes.labelsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
    'savefig.dpi': 300, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
    'axes.spines.top': False, 'axes.spines.right': False, 'mathtext.fontset': 'stix',
})
# Okabe-Ito colour-blind-safe palette
OI = {'blue': '#0072B2', 'orange': '#E69F00', 'grey': '#7F7F7F', 'verm': '#D55E00', 'green': '#009E73'}
def save_fig(fig, name):
    for ext in ('pdf', 'png'):
        fig.savefig(f'{name}.{ext}')
    print('Saved', name)
