import matplotlib.pyplot as plt
from pyfonts import load_google_font

# --- 1. FONTS ---
# Load font objects globally
try:
    BASE_FONT = load_google_font("Lato", weight="regular")
    BOLD_FONT = load_google_font("Lato", weight="black")
except ImportError:
    # Fallback to standard Matplotlib fonts if pyfonts is unavailable
    print("Warning: pyfonts not installed. Falling back to default Matplotlib fonts.")
    BASE_FONT = {'family': 'sans-serif', 'weight': 'normal'}
    BOLD_FONT = {'family': 'sans-serif', 'weight': 'bold'}

# --- 2. COLORS & THEME ---
COLORS = {
    'primary': '#03463b',
    'accent_strong': '#c4383c',
    'accent_light': '#e97a2a',
    'background_subtle': '#818d8b',
    'background_strong': '#e4e7e7',
    'text_general': '#20292c',
}

# --- 3. TEXT STYLES (Font Size and Weight) ---
TEXT_STYLES = {
    'heading':    {'size': 20, 'fontproperties': BOLD_FONT, 'color': COLORS['text_general']},
    'category':   {'size': 14, 'fontproperties': BASE_FONT, 'color': COLORS['text_general']},
    'annotation': {'size': 11, 'fontproperties': BASE_FONT, 'color': COLORS['primary']},
    'annotation_bold': {'size': 14, 'fontproperties': BOLD_FONT, 'color': COLORS['primary']},
    'tick_label': {'size': 12, 'fontproperties': BASE_FONT, 'color': COLORS['text_general']},
    'footer_text': {'size': 9, 'fontproperties': BASE_FONT, 'color': COLORS['text_general']},
    'unit_label': {'size': 11, 'fontproperties': BASE_FONT},
}

# --- 4. GLOBAL PLOT SETTINGS (optional but useful) ---
plt.rcParams['figure.dpi'] = 300