

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
    # reverse groups by reversing them in the groups list. Each list element is a group of 3.
    groups = [list(reversed(group)) for group in zip(*[list(s[i::3]) for i in range(3)])]
    # reverse each list element. The result is a string with each character repeated 3 times in the first 3 list elements.
    return "".join([group[-1] * (3 if len(group) > 1 else 1) for group in groups])

