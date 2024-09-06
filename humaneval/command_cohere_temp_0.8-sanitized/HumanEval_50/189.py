def encode_shift(s: str):
    """
    Encodes a string by shifting each character 5 steps in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    # Lazy encoder: Uses the alphabet size to determine the shift amount.
    return "".join([chr(((ord(ch) + 5 - 96) % 26) + 96) for ch in s])
def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input encoded string to be decoded.

    Returns:
        str: Decoded string.
    """
    return encode_shift(s)