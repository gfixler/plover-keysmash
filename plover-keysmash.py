import re
import random

LONGEST_KEY = 1

PLOVER_EXTENDED = True

TOP_S = "^" if PLOVER_EXTENDED else "S"

keymap = {
    "S": "qaz",
    "T": "ws",
    "K": "sx",
    "P": "ed",
    "W": "dc",
    "H": "rtfg",
    "R": "fgvb",
    "-F": "yuhj",
    "-R": "hjnm",
    "-P": "ik",
    "-B": "k,",
    "-L": "P;",
    "-G": ";/",
    "-T": "['",
    "-S": "'",
    "-D": "\\",
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

    for side, sep in [(left, ""), (right, "-")]:
        if side:
            for key in side:
                char = random.choice(keymap[sep + key])
                if shift and char in shifts:
                    pressed.append(shifts[char])
                else:
                    pressed.append(char)

    if pressed:
        random.shuffle(pressed)
        return "{&" + "".join(pressed) + "}"

    raise KeyError

