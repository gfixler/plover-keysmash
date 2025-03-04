import re
import random

LONGEST_KEY = 1

PLOVER_EXTENDED = True

TOP_S = "^" if PLOVER_EXTENDED else "S"

keymapLeft = {
    "S": "qaaz",
    "TK": "wssx",
    "T": "ws",
    "K": "sx",
    "PW": "eddc",
    "P": "ed",
    "W": "dc",
    "HR": "rtffggvb",
    "H": "rtfg",
    "R": "fgvb",
}

keymapRight = {
    "FR": "yuhhjjnm",
    "F": "yuhj",
    "R": "hjnm",
    "PB": "ikk,",
    "P": "ik",
    "B": "k,",
    "LG": "oll.",
    "L": "ol",
    "G": "l.",
    "TS": "p;;/",
    "T": "p;",
    "S": ";/",
    "D": "\\",
} | ({
    "^": "qa",
    "S": "az",
} if TOP_S else {})

numbers = {
    "^": "1",
    "S": "1",
    "T": "2",
    "P": "3",
    "H": "45",
    "-F": "6",
    "-P": "78",
    "-L": "9",
    "-T": "0",
}

shifts = {
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "(",
    "9": ")",
    "0": "-",
    "[": "{",
    "]": "}",
    "\\": "|",
    ";": ":",
    "'": "\"",
    ",": "<",
    "+": ">",
    "/": "?",
}

partsPattern = r"^(\^?S?T?K?P?W?H?R?)(?:-|(A?O?\*?E?U?))(F?R?P?B?L?G?T?S?D?Z?)$"
stenoParts = re.compile(partsPattern)

fromNums = "1234506789"
toLetters = TOP_S + "TPHAOFPLT"
denumberer = str.maketrans(fromNums, toLetters)

def lookup(outline):
    stroke = outline[0]

    denumbered = stroke.translate(denumberer)
    num_key_pressed = stroke != denumbered
    stroke = denumbered

    left, middle, right = re.match(stenoParts, stroke).groups()
    if middle is None:
        middle = ""

    shift = "A" in middle or "O" in middle or "D" in right

    pressed = []

    for entry in keymapLeft:
        if left.startswith(entry):
            char = random.choice(keymapLeft[entry])
            left = left[len(entry):]
            pressed.append(char)

    for entry in keymapRight:
        if right.startswith(entry):
            char = random.choice(keymapRight[entry])
            right = right[len(entry):]
            pressed.append(char)

    if pressed:
        random.shuffle(pressed)
        return "{&" + "".join(pressed) + "}"

    raise KeyError

