def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr((((ord(ch) - 96) % 26) + ord("a")) % 26 + 96) for ch in s])