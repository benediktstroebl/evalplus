Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.

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
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) % 26 >= 0 else ((ord(ch) - ord("a")) % 26 + 26)) or ord("a")) for ch in s])
```

This script defines two functions, `encode_shift` and `decode_shift`, as specified in the problem statement. The `encode_shift` function encodes a given string by shifting each character's ASCII value by 5, modulo 26, which ensures the shift is within the bounds of the alphabet. The `decode_shift` function decodes an encoded string back to its original form. This decoding process involves shifting the characters back by 5 and then using the modulo operation to remain within the ASCII range for alphabetic characters.