

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
    # replace each character with lower-case. Concatenate groups of 3.
    s = s.lower()
    s = "".join([s[(2 * i):min((2 * i + 2), len(s))] for i in range((len(s) + 1) // 2)])
    # split into groups of 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse each group.
    groups = [group[::-1] for group in groups]
    # keep first character for each group.
    groups = ["".join(groups[i][:1] + groups[i][2:]) for i in range(len(groups))]
    return "".join(groups)

