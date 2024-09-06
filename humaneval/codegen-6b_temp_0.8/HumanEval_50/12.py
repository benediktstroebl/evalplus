

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    d = {}
    for i, ch in enumerate(ascii_lowercase):
        d[ch] = i + 5
    i = 0
    ret = ""
    for ch in s:
        ret += ascii_lowercase[(d[ch] - i) % 26]
        i += 1
    return ret

