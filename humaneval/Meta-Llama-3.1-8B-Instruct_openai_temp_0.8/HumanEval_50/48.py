```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by iterating over each character in the string, 
    shifting it by 5 places in the alphabet, and adding the result as a character 
    to the encoded string. If the character is uppercase, it is shifted as 
    well, and then the ASCII value is adjusted to match the correct uppercase 
    character.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by iterating over each character in the string, 
    shifting it back by 5 places in the alphabet, and adding the result as a 
    character to the decoded string. If the character is uppercase, it is 
    shifted as well, and then the ASCII value is adjusted to match the correct 
    uppercase character.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Test the functions
if __name__ == "__main__":
    encoded = encode_shift("Hello, World!")
    print(f"Encoded: {encoded}")
    decoded = decode_shift(encoded)
    print(f"Decoded: {decoded}")
```

This script includes the `encode_shift` and `decode_shift` functions, which use the Caesar cipher to shift characters in the alphabet by 5 places. The `decode_shift` function is the inverse of `encode_shift`, and the `if __name__ == "__main__":` block is used to test the functions with a sample string.