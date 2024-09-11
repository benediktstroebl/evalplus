```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Test the functions
original_string = "Hello, World!"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original string: {original_string}")
print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_shift` function to shift every character in the input string `s` by 5 positions in the alphabet, wrapping around to the start of the alphabet if necessary. The `decode_shift` function is used to reverse this encoding process. The `isalpha` and `lower` methods are used to ensure that only alphabetic characters are shifted, and that the shift is case-insensitive. The script then tests these functions on the string "Hello, World!".