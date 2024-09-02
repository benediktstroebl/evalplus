

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
    # initialize list to store strings resulting from decoded procedure.
    strings = []
    # divide string in two.
    for i in range(0, len(s), 3):
        strings.append(s[i:i + 3])
    # take pairs, insert to new strings.
    return "".join([(string[2] + string[1]) if string[0] == string[1] else string for string in strings])

