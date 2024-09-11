```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character in the string to its ASCII value, 
    then shifting it by 5 positions in the alphabet (wrapping around to the start if necessary), 
    and finally converting it back to a character.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by first converting each character in the string to its ASCII value, 
    then shifting it by 5 positions back in the alphabet (wrapping around to the end if necessary), 
    and finally converting it back to a character.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Test the functions
s = "Hello, World!"
encoded = encode_shift(s)
decoded = decode_shift(encoded)
print(f"Encoded string: {encoded}")
print(f"Decoded string: {decoded}")
print(f"Original string: {s}")
```

This script provides two functions, `encode_shift` and `decode_shift`, which shift characters in a string by 5 positions in the alphabet. It uses the ASCII values of characters and the modulo operator to handle wrapping around to the start or end of the alphabet. The `isalpha` method is used to exclude non-alphabet characters from the encoding and decoding process. The script also includes a test section to demonstrate the functions' usage.