

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
    # create key which is 3 less than length of string.
    key = (len(s) - 3) % (len(s) // 3)
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse each group element.
    groups = [group[::-1] for group in groups]
    # if group length is less than 3, cycle last element into first element and add to first element.
    groups = [(groups[0][0] + groups[0][1] if len(groups[0]) < 3 else groups[0]) if len(groups[0]) == 3 else
              (groups[0][0] + groups[0][1] + groups[0][2]) if len(groups[0]) == 2 else groups[0]] + groups[1:]
    # add first element to end of string.
    groups[0] = groups[0] + groups[0][0]
    # add key to new string.
    groups[0] = groups[0][:-key] + encode_cyclic(groups[0][-key:])
    return "".join(groups)


