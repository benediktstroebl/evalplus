def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string to be decoded.
        
    Returns:
        str: Decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])