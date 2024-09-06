def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with encode_cyclic.
    """
    # Split string into groups of three
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling effect
    groups = [group[1:] + group[0] for group in groups[::-1]]
    return ''.join(groups)