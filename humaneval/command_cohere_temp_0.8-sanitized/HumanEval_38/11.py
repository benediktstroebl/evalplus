def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split the string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Restore the original order of characters in each group.
    decoded = [''.join(group)[i::3] for group in zip_longest(*groups, fillvalue='')]
    return ''.join(decoded)