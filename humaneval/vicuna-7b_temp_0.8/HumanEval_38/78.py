

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
    if s == "":
        return ""
    # split encoded string into groups. Each of length 3.
    groups = [s[3:min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse order of elements in each group to decoded string.
    groups = [(groups[i][::-1]) if len(groups[i]) == 3 else groups[i] for i in range(len(groups))]
    return "".join(groups)