def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with encode_cyclic.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle characters in each group to get original order.
    decoded = [''.join(group[1:] + group[0]) for group in groups if len(group) != 3]
    return ''.join(decoded)