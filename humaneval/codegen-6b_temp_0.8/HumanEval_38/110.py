

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
    # convert groups to list of lengths of each group.
    groups = [len(group) for group in s.split("")]
    # assume each group starts with 1 character (a) and ends with 1 character (b)
    groups = [(1 + groups[i]) if i == len(groups) - 1 else groups[i] for i in range(len(groups))]
    # add 1 to account for zero-indexing
    groups = [1 + i for i in groups]
    # convert lengths to groups
    groups = [s[-i:] if i < 3 else s[-i+2:-i] for i in groups]
    # convert groups to characters
    groups = [chr(ord('a') + i % 26) for i in groups]
    return "".join(groups)

