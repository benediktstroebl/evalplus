### Shift Encoder and Decoder
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) for ch in s if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script includes the `encode_shift` and `decode_shift` functions, which perform Caesar cipher-like encoding and decoding on a given string. The functions use the ASCII values of the characters in the string and the modulo operator to ensure that the encoding/decoding wraps around the alphabet.

The script also includes a simple example usage of the functions, where the original string "Hello, World!" is encoded and then decoded to demonstrate the functionality.