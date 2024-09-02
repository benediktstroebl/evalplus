

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
    # split input string into groups, each of length 3.
    groups = s.split(b'\x00')
    # rotate groups, such that each group starts with its last element,
    # and then reverse the rotation.
    groups = [groups[::-1].pop() + groups[1].pop() + groups[0].pop()]
    # reverse the order of elements in each group.
    groups = [[groups[i][::-1] for i in range(len(groups) - 1)] for groups in groups]
    # join the groups back to the original string.
    return "".join(groups)