

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
    cyclic_encoded_string = s
    decoded_string = ""
    for group in cyclic_encoded_string:
        # split group to three elements.
        elements = group.split("")
        # add first and last elements together.
        decoded_string += elements[0] + elements[len(elements) - 1]
        # cycle elements in group, unless group has fewer elements than 3.
        for i in range(1, len(elements)):
            decoded_string += elements[i]
    return decoded_string

