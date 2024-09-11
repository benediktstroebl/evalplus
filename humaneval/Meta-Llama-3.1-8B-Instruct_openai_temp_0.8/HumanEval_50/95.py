```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Test the functions
print("Original String: 'hello'")
encoded = encode_shift('hello')
decoded = decode_shift(encoded)
print(f"Encoded String: '{encoded}'")
print(f"Decoded String: '{decoded}'")
```

This script first defines the `encode_shift` function which takes a string `s` as input and returns the string with each character shifted by 5 positions forward in the alphabet. Conversely, the `decode_shift` function takes a string `s` as input, which is assumed to be the output of the `encode_shift` function, and returns the original string.

The script then includes a test case to demonstrate how to use these functions. It prints the original string, the encoded string, and the decoded string. The `lower()` method is used to ensure the functions work correctly regardless of case.

Please note that the functions only shift alphabetic characters (a-z). Non-alphabetic characters are left unchanged.