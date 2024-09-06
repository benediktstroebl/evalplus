def decode_shift(s: str):
    """
    Decodes an encoded string using the encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The original decoded string.
    """
    reverse_alphabet_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return ''.join(reverse_alphabet_map.get(ch, ch) for ch in s)