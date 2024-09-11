```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage
encoded_str = encode_shift("Hello, World!")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

Note that I've made some improvements:

1. I've added type hints and docstrings to make the code more readable.
2. I've used the `isalpha()` method to check if a character is a letter before trying to encode or decode it, to avoid errors.
3. I've used the `lower()` method to convert the input string to lowercase, so the encoding and decoding work correctly for uppercase letters as well.
4. I've used f-strings to make the output more readable.
5. I've added example usage at the end to demonstrate how to use the functions.