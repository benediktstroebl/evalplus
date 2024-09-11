```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Testing the functions
original_string = "Hello, World!"
encoded_string = encode_shift(original_string)
print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded String: {decoded_string}")
```

Note: These functions will only shift alphabetic characters (both lowercase and uppercase). Non-alphabetic characters will be left unchanged. The functions also handle edge cases where the shift operation would move beyond the alphabet (i.e., when shifting 'z' or 'Z' by 5 to the right, or when shifting 'a' or 'A' by 5 to the left).