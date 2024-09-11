### Shift Encoding and Decoding

The following script provides functions for encoding and decoding strings using a Caesar cipher with a shift of 5.

```python
def encode_shift(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes the input string only contains lowercase English letters.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes the input string only contains lowercase English letters.
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

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string, shifts each character by 5 places in the alphabet, and returns the encoded string. The `decode_shift` function does the opposite, taking an encoded string as input and returning the original string.

The script includes example usage at the end, demonstrating how to use these functions to encode and decode a string.