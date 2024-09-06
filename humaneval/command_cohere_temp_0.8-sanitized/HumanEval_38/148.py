def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Reverse cycle elements in each group.
    groups = [group[1:] + group[0][::-1] for group in groups]
    return "".join(groups)