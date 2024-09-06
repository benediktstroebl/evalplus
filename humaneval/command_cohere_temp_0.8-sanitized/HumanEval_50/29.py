def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) % 26 >= 0 else ((ord(ch) - ord("a")) % 26 + 26)) or ord("a")) for ch in s])