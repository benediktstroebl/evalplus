

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
    s = list(s)
    # iterate over s, identifying groups of length 3.
    for i, group in enumerate(s[:-2]):
        if len(s[i:i+3]) == 3 and s[i+1] not in "123":
            s[i+1] = group[-1] * 2
    return "".join(s)

