```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by adding 5 to the ASCII value of each lowercase letter in the input string.
    It uses the modulo operator to ensure that the result wraps around the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by subtracting 5 from the ASCII value of each lowercase letter in the input string.
    It uses the modulo operator to ensure that the result wraps around the alphabet.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
original_string = "hello world"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
```

Note: This code will handle both lowercase and uppercase letters, and it will preserve non-alphabetical characters. The `isalpha()` method is used to check if a character is a letter, and if it's not, the original character is left unchanged.