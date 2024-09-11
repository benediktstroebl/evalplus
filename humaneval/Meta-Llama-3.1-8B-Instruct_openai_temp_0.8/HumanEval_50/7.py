### Shift Encoder and Decoder
#### Encoding and Decoding Caesar Cipher

Here's an implementation of the `encode_shift` and `decode_shift` functions in Python.

```python
def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s if ch.isalpha()])

def decode_shift(s: str) -> str:
    """
    Decodes a string that was encoded with the encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) for ch in s if ch.isalpha()])

# Example usage:
input_str = "Hello, World!"
encoded_str = encode_shift(input_str)
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This code defines the `encode_shift` and `decode_shift` functions, which implement the Caesar cipher with a shift of 5. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `% 26` operation ensures that the shift wraps around the alphabet. The `isalpha` method is used to filter out non-alphabetic characters from the input string.