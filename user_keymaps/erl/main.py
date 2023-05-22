# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default

import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split, SplitSide
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# TODO Comment one of these on each side
# split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(
    # split_flip=True,
    data_pin=board.D1,
    split_side=split_side,
    split_target_left=False,
    # Using the default wasn't working, try pio
    use_pio=True,
    uart_flip=True,
)

layers = Layers()
holdtap = HoldTap()
mouse_key = MouseKeys()


keyboard.modules = [layers, split, mod_tap, mouse_key]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO


# Mod-taps: Layer 0
A_LGUI = KC.HT(KC.A, KC.LGUI)
S_LSFT = KC.HT(KC.S, KC.LSFT)
D_LCTL = KC.HT(KC.S, KC.LCTL)
S_LALT = KC.HT(KC.S, KC.LALT)
J_RALT = KC.HT(KC.J, KC.RALT)
K_RCTL = KC.HT(KC.K, KC.RCTL)
L_RSFT = KC.HT(KC.L, KC.RSFT)
P_RGUI = KC.HT(KC.P, KC.RGUI)
# Mod-taps: Layer 1
N1_LGUI = KC.HT(KC.N1, KC.LGUI)
N2_LSFT = KC.HT(KC.N2, KC.LSFT)
N3_LCTL = KC.HT(KC.N3, KC.LCTL)
N4_LALT = KC.HT(KC.N4, KC.LALT)
AD_RALT = KC.HT(KC.DOWN, KC.RALT)
AU_RCTL = KC.HT(KC.UP, KC.RCTL)
AR_RSFT = KC.HT(KC.RIGHT, KC.RSFT)
DL_RGUI = KC.HT(KC.DEL, KC.RGUI)
# Mod-taps: Layer 2
F6_LGUI = KC.HT(KC.F6, KC.LGUI)
F7_LSFT = KC.HT(KC.F7, KC.LSFT)
F8_LCTL = KC.HT(KC.F8, KC.LCTL)
F9_LALT = KC.HT(KC.F9, KC.LALT)
N8_RALT = KC.HT(KC.N8, KC.RALT)
N7_RCTL = KC.HT(KC.N7, KC.RCTL)
N6_RSFT = KC.HT(KC.N6, KC.RSFT)
N5_RGUI = KC.HT(KC.N5, KC.RGUI)

# Layer tap: Layer 0
L1_SPC = KC.LT(1, KC.SPC)
L2_ENT = KC.LT(2, KC.ENT)
TO__L1 = KC.TO(1)
# Layer tap: Layer 1
TO__L0 = KC.TO(0)
MO__L2 = KC.MO(2)
TO__L2 = KC.TO(2)
# Layer tap: Layer 2
TO__L1 = KC.TO(1)
MO__L3 = KC.MO(3)
TO__L3 = KC.TO(3)


# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # 0: Default
      KC.ESC,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O, KC.BSPC,
      A_LGUI,  S_LSFT,  D_LCTL,  S_LALT,    KC.G,    KC.H,  J_RALT,  K_RCTL,  L_RSFT,  P_RGUI,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.Q, KC.COLN, KC.EXLM,
                                KC.TAB,  L2_ENT,  L1_SPC,  TO__L1,
    ],
    [  # 1: Numbers (left), Navigation/Audio (right)
     XXXXXXX, XXXXXXX,   KC.N9, KC.LBRC, KC.QUOT, KC.HOME, KC.PGDN, KC.PGUP,  KC.END, _______,
     N1_LGUI, N2_LSFT, N3_LCTL, N4_LALT, KC.COMM, KC.RGHT, AD_RALT, AU_RCTL, AR_RSFT, DL_RGUI,
     KC.CAPS,  KC.GRV, KC.BSLS, KC.SCLN, XXXXXXX, KC.MUTE, KC.VOLU, KC.VOLD, KC.MPLY, KC.MSTP,
                                 TO__L0,  MO__L2, _______,  TO__L2,
    ],
    [  # 2: Function Keys (left), Numbers (right)
       KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5, KC.QUOT, KC.RBRC,   KC.N0, XXXXXXX, _______,
     F6_LGUI, F7_LSFT, F8_LCTL, F9_LALT,  KC.F10,  KC.DOT, N8_RALT, N7_RCTL, N6_RSFT, N5_RGUI,
      KC.F11,  KC.F12, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.SLSH, KC.MINS,  KC.EQL, XXXXXXX,
                                 TO__L1,  MO__L3, _______,  TO__L3,
    ],
    [  # RIGHT SYMBOLS
    _______, _______, _______, _______, _______, _______, KC.UNDS, KC.PIPE, KC.QUOT, _______,
    KC.CIRC, KC.ASTR, KC.AMPR, _______, _______, KC.HASH, KC.TILD, KC.SLSH, KC.DQUO,  KC.DLR,
    _______, _______, _______, _______, _______, _______, KC.MINS, KC.BSLS,  KC.GRV, _______,
                               _______, _______, _______, _______,
    ],
    [  # LEFT SYMBOLS
    _______, KC.COLN, KC.LABK, KC.RABK, KC.SCLN, _______, _______, _______, _______, _______,
    KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN,   KC.AT, _______, _______,  KC.EQL, KC.PLUS, KC.PERC,
    _______, KC.EXLM, KC.LBRC, KC.RBRC, _______, _______, _______, _______, _______, _______,
                               _______, _______, _______, _______,
    ],
    [  # 5 FUNCTION
    _______, _______, _______, _______, _______, _______, KC.F7, KC.F8, KC.F9, KC.F10,
    _______, _______, _______, _______, _______, _______, KC.F4, KC.F5, KC.F6, KC.F11,
    _______, _______, _______, _______, _______, _______, KC.F1, KC.F2, KC.F3, KC.F12,
                               _______, _______, _______, _______,
    ],
    [  # 6 NUMBERS
    KC.SLSH,   KC.N7,   KC.N8,   KC.N9, KC.PLUS, _______, _______, _______, _______, _______,
      KC.N0,   KC.N1,   KC.N2,   KC.N3, KC.MINS, _______, _______, _______, _______, _______,
    KC.ASTR,   KC.N4,   KC.N5,   KC.N6,  KC.EQL, _______, _______, _______, _______, _______,
                               _______, _______, _______, _______,
    ],
    [  # 7 ALWAYS AVAILABLE
    _______, _______, KC.COLN,  KC.ESC, _______, _______, _______, _______, _______,  KC.DEL,
    _______, KC.PERC, KC.SLSH,  KC.ENT, _______, KC.DF(1), KC.LGUI, _______, _______, _______,
    _______, _______, _______, KC.PERC, _______, KC.DF(0), KC.RALT, KC.RCTL, _______, KC.RESET,
                               _______,  KC.TAB, _______, _______,
    ],
]

if __name__ == "__main__":
    keyboard.go()
