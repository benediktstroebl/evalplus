def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
def decode_shift(s: str) -> str:
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return encode_shift(s)[5:]