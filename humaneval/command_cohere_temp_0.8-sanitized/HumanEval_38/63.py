def decode_cyclic(s: str) -> str:
    """
    Takes as input a string encoded with encode_cyclic function. Returns the decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Uncycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[0] + group[2:] if len(group) == 3 else group for group in groups]
    return ''.join(groups)