```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Test the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
    
    assert original_string == decoded_string, "Decoded string does not match original string"
    print("Test passed: Decoded string matches original string")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 places in the alphabet, while the `decode_shift` function reverses this operation to decode the string. The script also includes a test to verify that the decoding operation correctly restores the original string.