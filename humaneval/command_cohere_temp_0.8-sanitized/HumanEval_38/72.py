def decode_cyclic(s: str) -> str:
    """
    Decodes a string s encoded with the encode_cyclic function.
    Returns the decoded string.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling to get the original order.
    groups = [group[0] + group[2:] for group in groups]
    return ''.join(groups)