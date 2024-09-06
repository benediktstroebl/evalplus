def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input string to encode.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) % 26 > 4 else (((ord(ch) - ord("a")) % 26) - 5 + 26)) % 26) for ch in s])