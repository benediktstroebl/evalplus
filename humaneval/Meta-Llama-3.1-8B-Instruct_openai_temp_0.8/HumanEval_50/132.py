Here's a self-contained Python script that includes the `encode_shift` and `decode_shift` functions:
```markdown
# Shift Cipher Encoding and Decoding
=====================================

This script encodes and decodes a string by shifting every character by 5 positions in the alphabet.

### Code
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 positions in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Decodes a string that was encoded with the `encode_shift` function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    input_str = "Hello, World!"
    encoded_str = encode_shift(input_str)
    print(f"Encoded: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded: {decoded_str}")
```

### Explanation

*   The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet. It converts the input string to lowercase and only considers alphabetic characters.
*   The `decode_shift` function reverses the encoding process by shifting the characters back by 5 positions.
*   The example usage demonstrates how to use the `encode_shift` and `decode_shift` functions to encode and decode a string.