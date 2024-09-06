

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

    decoded = []
    # go through string and if group is not of length 3, add first element to decoded.
    for c in s:
        if len(decoded) == 0 or len(decoded[-1])!= 3:
            decoded.append(c)
            continue

        # go through group and add elements to decoded in order.
        for i in range(3):
            decoded.append(decoded[-1][1:])
            decoded[-1] = decoded[-1][0] + decoded[-1][:1]
    return "".join(decoded)

