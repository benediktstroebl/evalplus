```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Use a list comprehension to encode each character in the string
    encoded_chars = [chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]
    return "".join(encoded_chars)


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Use a list comprehension to decode each character in the string
    # The inverse operation of encode_shift is used here
    decoded_chars = [chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]
    return "".join(decoded_chars)


# Test the functions
if __name__ == "__main__":
    test_string = "Hello, World!"
    encoded_string = encode_shift(test_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script provides two functions, `encode_shift` and `decode_shift`, which perform Caesar cipher encoding and decoding with a shift of 5. The `% 26` operation ensures that the shift wraps around the alphabet if necessary. The `isalpha()` check is used to preserve non-alphabetic characters. A test string is encoded and then decoded to demonstrate the functionality.