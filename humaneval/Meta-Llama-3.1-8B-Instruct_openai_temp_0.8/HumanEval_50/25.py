```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    For lowercase letters, the shift is modulo 26. For other characters, no shift is applied.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if "a" <= ch <= "z" else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    For lowercase letters, the shift is modulo 26 in reverse. For other characters, no shift is applied.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) if "a" <= ch <= "z" else ch for ch in s])


# Example usage:
text = "hello"
encoded = encode_shift(text)
decoded = decode_shift(encoded)

print(f"Encoded text: {encoded}")
print(f"Decoded text: {decoded}")
```

This script defines two functions, `encode_shift` and `decode_shift`, which apply the Caesar cipher encryption and decryption to lowercase letters in a string. It then demonstrates the usage of these functions with a simple example.