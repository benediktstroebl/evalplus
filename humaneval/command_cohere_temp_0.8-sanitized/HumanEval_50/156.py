def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string encoded with encode_shift.
    
    Returns:
        str: Decoded string.
    """
    return "".join([chr((((ord(ch) - 96) % 26) + ord("a")) % 26 + 96) for ch in s])