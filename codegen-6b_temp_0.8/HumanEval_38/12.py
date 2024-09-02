

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # argument can only be length of string. Assume length is multiple of 3.
    length = len(s)
    lengths = [3, 2, 1, 0, length // 4, length // 6, length // 8, length // 12, length // 16, length // 24]
    lengths = [lengths[0], lengths[7]] + lengths[:-1]
    lengths = lengths[1:] + [lengths[0]]
    strings = [s[i:j] for i, j in zip(lengths, lengths[1:])]

    # undo any cycles by adding the first string back in the result.
    if length % 3 == 0:
        s = (s[0] + strings[0]) if strings[0] != "" else ""
    else:
        s = strings[0] * ((length - length % 3) // 3) + s

    return s

