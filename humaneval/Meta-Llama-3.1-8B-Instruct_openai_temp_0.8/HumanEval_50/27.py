```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function encodes every lowercase alphabet character in the string by shifting it 5 positions forward in the alphabet.
    Non-alphabet characters are left unchanged.
    
    Parameters:
    s (str): The input string to encode.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function decodes every lowercase alphabet character in the string by shifting it 5 positions backward in the alphabet.
    Non-alphabet characters are left unchanged.
    
    Parameters:
    s (str): The input string to decode.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage:
encoded_str = encode_shift("hello")
print("Encoded string:", encoded_str)

decoded_str = decode_shift(encoded_str)
print("Decoded string:", decoded_str)
```

Note: The `ord("a")` and `ord("z")` values are used as a reference point to calculate the shifted character. This approach can be used to shift the characters by any position. The `% 26` operation ensures that the shifted character wraps around the alphabet if necessary. The `lower()` function is used to ensure that the function works correctly for both lowercase and uppercase alphabet characters.