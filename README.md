# Plover Keysmash

One of the few missing things from a perfect stenography experience is the ability to mash on the keys, and get qwerty-style keymash. Steno is all chorded, so you end up outputting whole syllables, words, phrases, and "untrans" (all-caps, raw chords that didn't map to anything). If steno is going to compete with qwerty, we have to knock down such barriers to acceptance!

Note: I created this for the [Uni v4 from StenoKeyboards](https://stenokeyboards.com/products/the-uni-v4). If you have their [Polyglot](https://stenokeyboards.com/products/polyglot-keyboard), then you can just toggle over with one button to qwerty mode, and qwerty mash with actual qwerty, no need for this dictionary.

## Requirements

This is for the [Plover steno engine](https://github.com/openstenoproject/plover) software, so you'll need that installed.

You'll also need the [plover-python-dictionary](https://github.com/openstenoproject/plover_python_dictionary) plugin installed, as this is a python dictionary. Note: install this right from the Plover software (Tools → Plugin Manager).

Install something like the [plover-dict-commands](https://github.com/KoiOates/plover_dict_commands) plugin to allow toggling the dictionary on and off, again, right from the Plover software.

## Installation

Add the python file to your Plover dictionary list, at the top, if you're not sure where, and disable it.

Add a stroke to toggle the dictionary enable state. Mine is KPHARB, steno for KMASH.

## Usage

When you feel the need to key smash, qwerty-style, hit your toggle stroke to enable this dictionary, and mash away.
When you're sated, hit your toggle stroke again to return to steno mode.

# Design

1. the top row is the qwerty top row, and the bottom row is the qwerty bottom row
1. the qwerty middle row is accessed by stroking top and bottom row keys together
1. as there aren't enough keys, the following keys/chords make random choices:
    * H = "r" or "t"
    * R = "v" or "b"
    * HR = "f" or "g"
    * -F = "y" or "u"
    * -R = "n" or "m"
    * -FR = "h" or "j"
    * -D = "[" or "]" or "\\"
 
