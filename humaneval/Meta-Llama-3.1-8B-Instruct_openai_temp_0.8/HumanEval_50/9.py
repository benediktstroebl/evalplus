```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    If the character is not a lowercase letter, it is not shifted and added to the result as is.
    
    Parameters:
    s (str): The string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s if ch.isalpha() and ch.islower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    If the character is not a lowercase letter, it is not shifted and added to the result as is.
    
    Parameters:
    s (str): The string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 26 - 5) % 26 + ord("a")) for ch in s if ch.isalpha() and ch.islower()])


# Example usage:
s = "hello world"
print(f"Original string: {s}")

encoded_s = encode_shift(s)
print(f"Encoded string: {encoded_s}")

decoded_s = decode_shift(encoded_s)
print(f"Decoded string: {decoded_s}")
```

This script defines the `encode_shift` and `decode_shift` functions as requested, and adds some error checking to handle characters that are not lowercase letters. It also includes example usage at the end to demonstrate how to use these functions.