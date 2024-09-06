def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) % 26) + ord("a")) for ch in s])