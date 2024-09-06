Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded string:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input encoded string.

    Returns:
        str: Decoded string.
    """
    reverse_alphabet_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return ''.join(reverse_alphabet_map.get(ch, ch) for ch in s)
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes an input string and returns the encoded string by shifting each character by 5 in the alphabet. The `decode_shift` function takes an input encoded string and returns the original decoded string by shifting each character back by 5 in the alphabet. 

These functions can be called independently to encode or decode a string as shown in the provided tests. 
If you have more questions or need further assistance, feel free to ask!