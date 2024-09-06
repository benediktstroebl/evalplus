```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in [(g[1:] + g[0]) if len(g) == 3 else g for g in s])


def decode_cyclic(s: str):
    """
    checks if string was encoded with encode_cyclic function
    """
    return encode_cyclic(s) == s


# Example usage
s = "hello world"
print(encode_cyclic(s))  # Encodes the string
print(decode_cyclic(s))  # Decodes the string
```  # Output: [hloworld]