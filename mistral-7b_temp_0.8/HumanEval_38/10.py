

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
    # get length of encoded string.
    length = len(s)
    # length of encoded string % 3 = 1, 2 or 0. 1 or 2 means that decoding would not restore original string.
    if length % 3:
        raise Exception("Cyclic encoding can only be applied to strings of length which is multiple of 3")
    # split encoded string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), length)] for i in range(length // 3)]
    # get the head of each group.
    group_heads = [group[0] for group in groups]
    # get the tail of each group.
    group_tails = [group[1:] for group in groups]
    # decode each group.
    decoded_groups = [(group_head + group_tail) for group_head, group_tail in zip(group_heads, group_tails)]
    # join decoded groups.
    return "".join(decoded_groups)

