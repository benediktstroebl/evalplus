Here's a Python script with a self-contained function that solves the problem you've described, along with a script to decode the encoded string:
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
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) % 26) + ord("a")) for ch in s])

# Unit tests:
assert encode_shift("Hello, World!") == "If, Jbgmw, Bmjjv, Qn, Uxmpj, Ngjvkji, Cjh, Zlujg, Ic, Dxmd"
assert decode_shift("If, Jbgmw, Bmjjv, Qn, Uxmpj, Ngjvkji, Cjh, Zlujg, Ic, Dxmd") == "Hello, World!"
```
The `encode_shift` function shifts each character of the input string by 5 in the alphabet, with the modulo 26 ensuring that the encoding stays within the English alphabet, while the `decode_shift` function decodes the encoded string using a similar algorithm.

This script includes a few unit tests to validate the functionality of these functions. Let me know if you need assistance understanding any part of the code or if you'd like me to explain any concept used here.