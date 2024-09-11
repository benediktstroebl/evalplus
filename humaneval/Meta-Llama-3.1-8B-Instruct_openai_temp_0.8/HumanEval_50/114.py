### Caesar Cipher Encoder and Decoder
#### Overview

This Python script implements a simple Caesar cipher encoder and decoder. The encoder shifts every character in the input string by 5 positions in the alphabet, while the decoder reverses this process to restore the original text.

#### Code
```markdown
def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting every character by 5 positions in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str) -> str:
    """
    Decodes a string that was encoded using the encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```
#### Explanation

*   The `encode_shift` function shifts every lowercase letter in the input string by 5 positions in the alphabet. Non-alphabetic characters are left unchanged.
*   The `decode_shift` function reverses the encoding process, shifting every lowercase letter back by 5 positions in the alphabet.
*   The example usage at the end demonstrates the encoding and decoding of a sample string.

Feel free to modify or extend this script as needed.