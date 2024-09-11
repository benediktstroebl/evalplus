### Caesar Cipher Encoder and Decoder
#### Problem Statement
Write a Python script that encodes and decodes strings using a Caesar cipher with a shift of 5.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    result = ""
    for ch in s:
        if ch.isalpha():
            ascii_offset = ord("a") if ch.islower() else ord("A")
            result += chr(((ord(ch) - ascii_offset + 5) % 26) + ascii_offset)
        else:
            result += ch  # non-alphabetic characters remain unchanged
    return result

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return encode_shift(s)  # since decoding is equivalent to encoding with a shift of -5


# Example usage:
if __name__ == "__main__":
    original_str = "Hello, World!"
    encoded_str = encode_shift(original_str)
    decoded_str = decode_shift(encoded_str)
    
    print("Original string:", original_str)
    print("Encoded string:", encoded_str)
    print("Decoded string:", decoded_str)
    print("Decoded string (equivalent to original):", decoded_str == original_str)
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabetic character in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function is equivalent to applying the `encode_shift` function with a shift of -5, effectively reversing the encoding. The example usage demonstrates the encoding and decoding of a string.