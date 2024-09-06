def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer than 3 elements.
    groups = [group[1:] + group[0] for group in groups if len(group) == 3]
    return "".join(groups)
def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    return encode_cyclic(s[1:] + s[0])