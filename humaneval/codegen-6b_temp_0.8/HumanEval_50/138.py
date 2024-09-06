

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    # we have to find the shift and check that it's valid.
    # ord("a") + 5 - ord("a") % 26 = 0.
    shift = ord("a") + 5 - ord("a") % 26

    return "".join([chr(((ord(ch) - shift - ord("a")) % 26) + ord("a")) for ch in s])

