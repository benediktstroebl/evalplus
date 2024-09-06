def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    reverse_alphabet_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return ''.join(reverse_alphabet_map.get(ch, ch) for ch in s)