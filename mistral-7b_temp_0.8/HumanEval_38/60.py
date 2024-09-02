

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
    # convert every second character to a list of three characters.
    s = list(s)
    for i in range(len(s)):
        s[i] = list(s[i])
    # convert each character into an integer between 0 and 63.
    s = [chr(ord(c) - 97) for c in s]
    s = [int(i) for i in s]
    # unzip list of list of lists to list of lists.
    s = [tuple(x) for x in zip(*s)]
    s = list(s)
    # convert list of lists to list of strings.
    s = ["".join(map(str, l)) for l in s]
    return "".join(s)

