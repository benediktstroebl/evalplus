

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
    # split string to groups of length 2 or 3.
    groups = [s[(2 if i % 2 == 0 else 3) * i:min(((2 if i % 2 == 0 else 3) * i + 2, len(s)))]
              for i in range(len(s) // 2 + 1)]
    # if group has length 2, then first char is last char, else first char is first char.
    groups = [(group[0] + group[1:]) if len(group) == 2 else group for group in groups]
    return "".join(groups)

