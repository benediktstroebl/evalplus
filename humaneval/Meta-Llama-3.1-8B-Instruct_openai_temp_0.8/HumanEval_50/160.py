```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]).lower()


# Example usage
s = "Hello, World!"
encoded = encode_shift(s)
print(f"Encoded: {encoded}")

decoded = decode_shift(encoded)
print(f"Decoded: {decoded}")
```

This Python script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function encodes a given string by shifting each letter by 5 positions in the alphabet. If the input string contains non-alphabetic characters, they remain unchanged. The `decode_shift` function reverses this process to decode the string. Both functions handle lowercase and uppercase letters correctly, preserving the original case of the input string. The example usage at the end demonstrates how to use these functions to encode and decode a string.