def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling effect.
    decoded = [''.join(group) for group in groups]
    return ''.join(decoded)