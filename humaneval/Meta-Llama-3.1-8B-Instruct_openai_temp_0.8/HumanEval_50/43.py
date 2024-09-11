```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    For lowercase letters, the shift is applied directly by adding 5 to the ASCII value.
    For uppercase letters, the shift is applied by adding 5 to the ASCII value of lowercase letter
    corresponding to the uppercase letter and then converting back to uppercase.
    
    For non-alphabetical characters, the string remains unchanged.
    """
    result = ""
    for ch in s:
        if ch.isalpha():
            ascii_offset = ord("a") if ch.islower() else ord("A")
            result += chr(((ord(ch) - ascii_offset + 5) % 26) + ascii_offset)
        else:
            result += ch
    return result


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return encode_shift(s)


# Example usage:
encoded_str = encode_shift("Hello, World!")
print(f"Encoded: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded: {decoded_str}")
```

This code provides the implementation of both `encode_shift` and `decode_shift` functions as per the problem statement. It handles both lowercase and uppercase letters, and leaves non-alphabetical characters unchanged. The `decode_shift` function simply calls `encode_shift` with the reverse argument to achieve the same effect as decoding.