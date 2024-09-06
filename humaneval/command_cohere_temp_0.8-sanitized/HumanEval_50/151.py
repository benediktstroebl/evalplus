def decode_shift(s: str):
    """
    Decodes a string encoded with the `encode_shift` function.
    """
    reverse_alpha_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return "".join([reverse_alpha_map.get(ch, ch) for ch in s])