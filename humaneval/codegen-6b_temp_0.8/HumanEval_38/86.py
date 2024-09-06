

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
    # length of input string.
    length = len(s)
    # each group of three characters.
    groups = [s[(3 * i):min((3 * i + 3), length)] for i in range((length + 2) // 3)]
    # take first and last from each group.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # return as join of strings.
    return "".join(groups)

