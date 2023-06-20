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
split_side = SplitSide.LEFT
# split_side = SplitSide.RIGHT
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


# Mod-tap:
A_LGUI = KC.HT(KC.A, KC.LGUI)
S_LSFT = KC.HT(KC.S, KC.LSFT)
D_LCTL = KC.HT(KC.S, KC.LCTL)
S_LALT = KC.HT(KC.S, KC.LALT)
J_RALT = KC.HT(KC.J, KC.RALT)
K_RCTL = KC.HT(KC.K, KC.RCTL)
L_RSFT = KC.HT(KC.L, KC.RSFT)
P_RGUI = KC.HT(KC.P, KC.RGUI)

# Layer and Layer-tap:
L1_SPC = KC.LT(1, KC.SPC)
L1_ENT = KC.LT(1, KC.ENT)
L2___G = KC.LT(2, KC.G)
L2___H = KC.LT(2, KC.H)
L3___T = KC.LT(3, KC.T)
L3___Y = KC.LT(3, KC.Y)
TO__L0 = KC.TO(0)
TO__L1 = KC.TO(1)
TO__L2 = KC.TO(2)
TO__L3 = KC.TO(3)

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # 0: Default
      KC.ESC,    KC.W,    KC.E,    KC.R,  L3___T,  L3___Y,    KC.U,    KC.I,    KC.O, KC.BSPC,
      A_LGUI,  S_LSFT,  D_LCTL,  S_LALT,  L2___G,  L2___H,  J_RALT,  K_RCTL,  L_RSFT,  P_RGUI,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.Q, KC.COMM,  KC.DOT,
                                KC.TAB,  L1_ENT,  L1_SPC,  TO__L1,
    ],
    [  # 1: Symbols
     KC.PLUS, KC.PIPE, KC.QUES, KC.UNDS, KC.DQUO, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.COLN,
      KC.EQL, KC.BSLS, KC.SLSH, KC.MINS, KC.QUOT, KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.SCLN,
     KC.TILD, KC.LPRN, KC.LCBR, KC.LBRC, KC.LABK, KC.RABK, KC.RBRC, KC.RCBR, KC.RPRN, KC.MSTP,
                                 TO__L0, _______, _______,  TO__L2,
    ],
    [  # 2: Numbers and Navigation
     XXXXXXX,   KC.N7,   KC.N8,   KC.N9, XXXXXXX, KC.HOME, KC.PGDN, KC.PGUP,  KC.END, KC.CAPS,
     XXXXXXX,   KC.N4,   KC.N5,   KC.N6, XXXXXXX, KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT,  KC.DEL,
       KC.N0,   KC.N1,   KC.N2,   KC.N3, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                 TO__L1, _______, _______,  TO__L3,
    ],
    [  # 3: Function Keys and Media Keys
      KC.F12,   KC.F7,   KC.F8,   KC.F9, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
      KC.F11,   KC.F4,   KC.F5,   KC.F6, XXXXXXX, KC.MUTE, KC.VOLD, KC.VOLU, XXXXXXX, XXXXXXX,
      KC.F10,   KC.F1,   KC.F2,   KC.F3, XXXXXXX, KC.MPLY, KC.MPRV, KC.MNXT, KC.MSTP, XXXXXXX,
                                 TO__L2, _______, _______,  TO__L0,
    ],
]

if __name__ == "__main__":
    keyboard.go()
