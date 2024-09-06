

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
    # converts string to list of lists of length 3.
    groups = [[s[i], s[i + 1], s[i + 2]] for i in range(0, len(s), 3)]
    # inverts list of lists, getting cyclic groups.
    groups = [list(reversed(group)) for group in groups]
    # adds first characters to each list.
    groups = ["".join(group) for group in groups]
    return "".join(groups)

