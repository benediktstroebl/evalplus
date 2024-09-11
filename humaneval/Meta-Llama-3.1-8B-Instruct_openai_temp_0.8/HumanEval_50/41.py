## Caesar Cipher Encoder and Decoder

Below is a Python script that implements a Caesar cipher encoder and decoder.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string
    
    Returns:
    str: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string
    
    Returns:
    str: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage
s = "Hello, World!"
encoded = encode_shift(s)
decoded = decode_shift(encoded)

print(f"Original String: {s}")
print(f"Encoded String: {encoded}")
print(f"Decoded String: {decoded}")
```

This script first converts the input string to lowercase to simplify the encoding and decoding process. It then uses the Caesar cipher algorithm to shift each character by 5 positions in the alphabet. The `isalpha()` method is used to filter out non-alphabetic characters.

When you run this script, it will print the original string, the encoded string, and the decoded string.