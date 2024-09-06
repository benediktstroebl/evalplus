def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return encode_shift(s, shift=(-5))