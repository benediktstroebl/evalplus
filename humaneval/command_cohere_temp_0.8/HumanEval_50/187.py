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
    reverse_alphabet_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return ''.join(reverse_alphabet_map.get(ch, ch) for ch in s)
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes an input string and returns an encoded string, where each character is shifted by 5 in the alphabet. The `decode_shift` function takes an input string and returns a decoded string, undoing the encoding process. This pair of functions allows you to encode and then decode a string, providing a basic encryption and decryption functionality.