### Shift Encoder and Decoder

The following Python code contains a solution to the given problem. It includes a `encode_shift` function to encode a string by shifting every character by 5 in the alphabet, and a `decode_shift` function to decode the encoded string.

```markdown
### shift_encoder_decoder.py

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    The encoding is based on the assumption that the input string only contains lowercase English letters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    The decoding is based on the assumption that the input string only contains lowercase English letters.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script will first encode a given string by shifting every character by 5 in the alphabet, then it will decode the encoded string back to the original string. The `encode_shift` function uses the formula `(ord(ch) - ord("a") + 5) % 26` to shift characters in the alphabet, and the `decode_shift` function uses the formula `(ord(ch) - ord("a") - 5) % 26` to shift characters back in the alphabet.

When you run this script, you will see the original string, the encoded string, and the decoded string printed in the console. The decoded string should be the same as the original string.

**Note:** This script assumes that the input string only contains lowercase English letters. If the input string contains uppercase letters or other characters, the encoding and decoding will not work correctly.