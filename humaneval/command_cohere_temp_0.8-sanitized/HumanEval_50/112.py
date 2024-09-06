def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input encoded string.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if ((ord(ch) - ord("a")) % 26) - 5 >= 0 else ((ord(ch) - ord("a")) % 26) - 5 + 26)) for ch in s])