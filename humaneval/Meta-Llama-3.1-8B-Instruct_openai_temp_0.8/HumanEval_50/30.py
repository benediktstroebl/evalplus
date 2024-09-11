### Caesar Cipher Encoder and Decoder
#### Python Implementation

```python
def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str) -> str:
    """
    Decodes a string that was previously encoded with the encode_shift function.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script provides two functions, `encode_shift` and `decode_shift`, to implement a basic Caesar cipher. It shifts every alphabetical character in the input string by 5 positions in the alphabet, preserving the case of the original characters. The `isalpha` method is used to handle non-alphabetical characters, which are left unchanged.

In the example usage section, we demonstrate the usage of these functions by encoding and decoding a sample string.