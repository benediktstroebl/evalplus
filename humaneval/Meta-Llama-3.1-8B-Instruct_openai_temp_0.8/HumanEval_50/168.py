```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    Only lower case letters are shifted, others remain unchanged.
    
    Parameters:
    s (str): input string
    
    Returns:
    str: encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): encoded string
    
    Returns:
    str: decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
input_string = "hello, world!"
encoded = encode_shift(input_string)
decoded = decode_shift(encoded)

print("Encoded string:", encoded)
print("Decoded string:", decoded)
```

This script encodes a given string by shifting every lower case letter by 5 in the alphabet and keeps other characters unchanged. The `decode_shift` function then reverses this encoding to get back the original string. The example usage demonstrates how to use these functions to encode and decode a string.