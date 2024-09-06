

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
    # determine length of string by looking at first character.
    length = len(s)
    # if even, divide by 2. If odd, double it and add 1.
    if length % 2 == 0:
        length = length // 2
    else:
        length = (length + 1) // 2
    # repeat each group of three characters. Use * instead of +.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range(length)]
    groups = ["*" + group[1:] + group[0] if len(group) == 3 else group for group in groups]
    # join groups together.
    return "".join(groups)

