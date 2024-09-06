

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
    # map each group to int, ordered by their most common appearance.
    s_dict = Counter(s)
    # create lists of lists. Each list is a group.
    groups = [[] for _ in range(len(s_dict))]
    for group, count in s_dict.items():
        groups[count].append(group)
    # convert each group to a string and put in list, return the list
    output = [''.join(group) for group in groups]
    return "".join(output)

