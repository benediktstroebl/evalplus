def decode_shift(s: str):
    """
    Decodes a string encoded with the `encode_shift` function.
    """
    reverse_alphabet_offset = ord("z") - ord("a") + 1
    return "".join([chr((ord(ch) - ord("a") - 5) % reverse_alphabet_offset + ord("a")) for ch in s])