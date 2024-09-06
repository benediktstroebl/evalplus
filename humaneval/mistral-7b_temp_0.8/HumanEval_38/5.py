

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
    # split encoded string into groups of 3 characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # split each group into two parts: the first 2 characters and the third.
    group_parts = [group[0:2], group[2]] for group in groups]
    # create dictionary of pairs in the original string.
    pairs = {}
    for group in group_parts:
        pairs[group] = pair.group(2) + group[0]
    return "".join(pairs)

