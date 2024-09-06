

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
    # invert cycle. If length of s is not a multiple of 3, then the last char is shifted one place
    # and so on until length of s is a multiple of 3.
    s = s + s[0] * ((len(s) // 3) * 3 + 2)
    inverted_s = s[::-1]

    # use a split function to split into groups of 3 chars.
    groups = [inverted_s[(3 * i):min((3 * i + 3), len(inverted_s))] for i in range((len(inverted_s) + 2) // 3)]

    # use a join function to join each group to form new string.
    return "".join([group[1:] + group[0] for group in groups])