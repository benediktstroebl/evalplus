```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: Input encoded string
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
s = "hello world"
encoded = encode_shift(s)
print(f"Encoded: {encoded}")

decoded = decode_shift(encoded)
print(f"Decoded: {decoded}")
```

In this script, the `encode_shift` function shifts every character in the input string by 5 positions in the alphabet. The `decode_shift` function reverses this process to decode the string. Note that this code preserves the case of the original characters and leaves non-alphabetic characters unchanged.