def decode_shift(string):
    """
    Decodes an encoded string using the encode_shift function.
    Args:
        string (str): Input string encoded with encode_shift function.

    Returns:
        str: Original decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in string])