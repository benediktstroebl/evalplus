

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
    # split input string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # split groups to pairs. First pair is the first element of the group.
    # Second pair is the group's element at index 2, and the group's element at index 1.
    first_pair, second_pair = [], []
    for group in groups:
        first_pair.append(group[0])
        second_pair.append(group[1:2] + group[2:3])
    # convert pairs to decoded string.
    return "".join([pair[1] + pair[0] for pair in zip(first_pair, second_pair)])
