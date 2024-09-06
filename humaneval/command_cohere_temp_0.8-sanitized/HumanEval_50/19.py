def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])