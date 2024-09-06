def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) >= 0 else ((ord(ch) - ord("a")) % 26)) or ord("a")) for ch in s])