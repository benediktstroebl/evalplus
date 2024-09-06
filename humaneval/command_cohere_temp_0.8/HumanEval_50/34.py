Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded string:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    reverse_alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([reverse_alphabet[ord(ch) - ord(reverse_alphabet[0]) + ord("a")] for ch in s])
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns the encoded version of the string, where each character is shifted by 5 in the alphabet. The `decode_shift` function takes an encoded string as input and returns the original string. You can use these functions together to encode and decode strings as needed.