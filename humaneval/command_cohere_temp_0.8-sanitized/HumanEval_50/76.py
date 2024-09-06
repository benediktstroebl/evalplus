def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
        s (str): Input string encoded with encode_shift.
        
    Returns:
        str: Decoded string.
    """
    # Translate every character in the string back by subtracting 5 from its ASCII value and wrapping around the alphabet.
    return "".join([chr((((ord(ch) - 96) % 26) - 5) % 26) for ch in s])