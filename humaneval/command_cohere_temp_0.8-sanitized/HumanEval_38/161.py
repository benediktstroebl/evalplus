def decode_cyclic(s: str) -> str:
    """
    Decodes a string s encoded with the encode_cyclic function.
    Returns the decoded string.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle characters in each group.
    decoded = [group[0] + group[2:] for group in groups if len(group) == 3]
    return ''.join(decoded)