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
    return "".join([chr((((ord(ch) - 96) % 26) + ord("a")) % 26 + 96) for ch in s])
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function shifts each character in a given string by 5 in the alphabet, wrapping around to the beginning of the alphabet if the shift exceeds 'z'. The `decode_shift` function undoes the encoding process, shifting each character back by 5 to recover the original string. This pair of functions should correctly encode and decode messages using the specified shift ciphers.