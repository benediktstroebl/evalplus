def decode_cyclic(s: str) -> str:
    """
    Decodes a string s encoded with the encode_cyclic function.
    Returns the decoded string.
    """
    # Split the encoded string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling in each group.
    decoded = [group[1:] + group[0][::-1] for group in groups]
    return ''.join(decoded)