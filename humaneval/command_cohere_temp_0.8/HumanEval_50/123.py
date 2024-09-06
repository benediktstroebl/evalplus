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
    Decodes an encoded string using the encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The original decoded string.
    """
    reverse_alpha_map = {chr(ord("a") + n): chr(ord("a") + (n - 5)) for n in range(1, 27, 5)}
    return "".join(reverse_alpha_map.get(ch, ch) for ch in s)
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes an input string and shifts each character by 5 in the alphabet to obtain the encoded string. The `decode_shift` function takes an encoded string obtained from `encode_shift` and returns the original decoded string by reversing the shift operation for each character. This script provides a concise solution to the problem while maintaining code readability and functionality.