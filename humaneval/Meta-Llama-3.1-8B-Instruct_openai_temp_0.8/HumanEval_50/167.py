```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): input string to be encoded.
    
    Returns:
    str: encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): input string to be decoded.
    
    Returns:
    str: decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Testing the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    print(f"Original String: {original_string}")
    
    encoded_string = encode_shift(original_string)
    print(f"Encoded String: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

In the code above, the `encode_shift` function shifts every alphabetic character in the input string by 5 positions in the alphabet. The `decode_shift` function does the opposite of `encode_shift`, shifting every character back by 5 positions.

Note that the code only shifts alphabetic characters and leaves other characters (like spaces and punctuation) unchanged. The modulo operation (`% 26`) ensures that the shift wraps around the alphabet, so 'z' shifted by 5 becomes 'v'.