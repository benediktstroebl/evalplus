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
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])

# Example usage:
input_str = "hello world"
encoded_str = encode_shift(input_str)
decoded_str = decode_shift(encoded_str)

print("Input string:", input_str)
print("Encoded string:", encoded_str)
print("Decoded string:", decoded_str)
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet when necessary. The `decode_shift` function reverses this process to recover the original string.

The example usage at the end demonstrates how to use these functions to encode and decode a string.