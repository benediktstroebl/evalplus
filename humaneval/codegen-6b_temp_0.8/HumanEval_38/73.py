

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
    # cycle each element of each group. If group has fewer than 3 elements, take the rest of the
    # elements as a new group.
    groups = [
        (s[(3 * i):min(3 * i + 3, len(s))] for i in range(len(s) // 3))
        if len(s) % 3 == 0
        else [(s[(3 * i):]) for i in range(len(s) // 3 + 1)]
    ]
    # join groups to form new string.
    return "".join(["".join(i) for i in groups])

