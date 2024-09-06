

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
    length = len(s)
    # as required by the description, we need to add one more character to the end of the encoded string.
    while len(s) % 3 != 0:
        s += 'a'
    # split into 3-character groups and reverse their positions.
    groups = [s[(3 * i):min((3 * i + 3), len(s))][::-1] for i in range((len(s) + 2) // 3)]
    # join the groups to form the decoded string.
    return "".join(groups)

