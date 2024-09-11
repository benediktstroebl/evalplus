```markdown
### Caesar Cipher Encoder and Decoder

This script implements a simple Caesar cipher encoding and decoding using Python.

#### Code
```python
def encode_shift(s: str):
    """
    Returns an encoded string by shifting every character by 5 in the alphabet.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Parameters:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print("Original String:", original_string)
    print("Encoded String:", encoded_string)
    print("Decoded String:", decoded_string)
```

#### Explanation

The `encode_shift` function works by shifting each character in the input string by 5 positions in the alphabet. It uses the ASCII values of the characters to perform this operation. The `% 26` operation ensures that the result wraps around to the start of the alphabet if it exceeds 'z'.

The `decode_shift` function is the inverse of `encode_shift` and works similarly, but with a negative shift value.

In the example usage, we demonstrate the encoding and decoding of a string using these functions.
```