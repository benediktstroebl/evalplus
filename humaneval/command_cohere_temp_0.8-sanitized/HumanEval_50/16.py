def decode_shift(s: str):
    """
    Decodes an encoded string using the encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The original decoded string.
    """
    reverse_alpha_map = {chr(ord("a") + n): chr(ord("a") + (n - 5)) for n in range(1, 27, 5)}
    return "".join(reverse_alpha_map.get(ch, ch) for ch in s)