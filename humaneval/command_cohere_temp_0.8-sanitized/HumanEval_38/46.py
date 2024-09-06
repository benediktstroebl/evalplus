def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split the string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Restore the original order by cycling.
    decoded = [''.join(group) for group in groups if len(group) == 3]
    return ''.join(decoded)