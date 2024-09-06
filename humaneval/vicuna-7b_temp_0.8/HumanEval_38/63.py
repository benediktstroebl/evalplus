

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
    # split input string into groups of 3 characters.
    groups = s.split("")
    # get number of groups in the input string
    num_groups = len(groups) // 3
    # reshape groups to have 3 elements each.
    reshaped_groups = [groups[i:i+3] for i in range(0, len(groups), 3)]
    # apply the cyclic rotation on each reshaped group
    reshaped_groups = [((j + 1) % 3) + (j // 3) + (j % 3) for j in reshaped_groups]
    # concatenate the reshaped groups to form the decoded string
    return "".join(reshaped_groups)
