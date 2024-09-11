### Shift Encoding and Decoding Script
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s
                    if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
    s (str): Input string to be decoded.

    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s
                    if ch.isalpha()])


# Example usage:
original_string = "hello"
encoded_string = encode_shift(original_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```
This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns a new string where each alphabetic character is shifted by 5 positions in the alphabet. The `decode_shift` function does the opposite, taking an encoded string as input and returning the original string.

The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `isalpha` method checks if a character is alphabetic.

The example usage demonstrates how to use these functions to encode and decode a string.