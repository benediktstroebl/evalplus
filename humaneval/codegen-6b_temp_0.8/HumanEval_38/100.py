

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
    # compute size of returned string
    length = len(s) * 3 + 2
    # preallocate a string of size length filled with '_'
    return_string = ['_' for _ in range(length)]
    # compute number of cycles
    cycles = len(s) + 1
    # prefix each element of the string with a '_'
    return_string[0] = '_'
    # place each group (of 3 characters) into the slots we need.
    for i in range(cycles):
        return_string[(3 * i):min((3 * i + 3), length)] = s[i % len(s)]
    # place the return_string with the last '_'
    return_string[-1] = '_'
    # reverse sort the bits
    return "".join(sorted(return_string, key=lambda x: x != '_'))

