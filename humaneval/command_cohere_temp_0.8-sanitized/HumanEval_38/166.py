def decode_cyclic(s: str) -> str:
    """
    Decodes a string s encoded with the encode_cyclic function.
    Returns the decoded string.
    """
    # Split the string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling to decode.
    decoded = [group[1:] + group[0] for group in groups[::-1]]
    return ''.join(decoded)