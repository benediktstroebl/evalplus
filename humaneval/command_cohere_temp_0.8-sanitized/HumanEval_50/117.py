def encode_shift(string: str) -> str:
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Args:
        string (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in string])
def decode_shift(string: str) -> str:
    """
    Decodes an encoded string using the encode_shift function.

    Args:
        string (str): The encoded string to be decoded.

    Returns:
        str: The original decoded string.
    """
    return encode_shift(string)