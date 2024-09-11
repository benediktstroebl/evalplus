```markdown
# Shift Encoder and Decoder
=====================================

This script provides two functions to encode and decode strings by shifting every character by 5 places in the alphabet.

### Function: encode_shift

Encodes a string by shifting every character by 5 places in the alphabet.

### Function: decode_shift

Decodes a string that was encoded with the `encode_shift` function.

### Code

```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 places in the alphabet.

    Args:
        s (str): The string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Decodes a string that was encoded with the encode_shift function.

    Args:
        s (str): The encoded string.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print("Encoded String:", encoded_string)
    decoded_string = decode_shift(encoded_string)
    print("Decoded String:", decoded_string)
```

### Explanation

The `encode_shift` function uses the ASCII values of the characters in the alphabet to shift every character by 5 places. It first converts the input string to lowercase, then it checks if each character is a letter. If it is, it calculates the encoded character by subtracting the ASCII value of 'a', adding 5, taking the modulus 26 (to wrap around the alphabet), and then adding the ASCII value of 'a' back. If the character is not a letter, it is left unchanged.

The `decode_shift` function is similar, but it subtracts 5 instead of adding it to shift the characters back in the opposite direction.

The example usage at the end demonstrates how to use these functions to encode and decode a string.