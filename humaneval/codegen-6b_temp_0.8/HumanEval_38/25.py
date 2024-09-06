

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
    # get group lengths
    group_lengths = [len(x) for x in s]
    # take first group length
    first_group_length = group_lengths[0]
    # create new list of strings 
    new_groups = [(s[(first_group_length * i):min((first_group_length * i + first_group_length))]) for i in range((len(s) + 2) // first_group_length)]
    # zip elements
    groups = zip(new_groups, group_lengths[1:])
    # join zipped elements
    groups = [''.join(g) for g in groups]
    # remove first element
    groups.pop(0)
    return ''.join(groups)
