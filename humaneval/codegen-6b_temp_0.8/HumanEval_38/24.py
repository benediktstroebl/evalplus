

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
    # decode string by decoding each group.
    groups = [iter(s)] * 3
    groups = [group if len(group) == 3 else group + group[len(group) - 1] for group in groups]
    # empty string.
    decoded = ""
    for group in groups:
        # if group has 3 elements, concatenate three to one element.
        decoded += group[0] + group[1] + group[2]
    return decoded

