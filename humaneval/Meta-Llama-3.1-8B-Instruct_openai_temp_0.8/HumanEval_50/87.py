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


# Example usage
original_string = "Hello World"
encoded_string = encode_shift(original_string)
print(f"Encoded string: {encoded_string}")
decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabetic character in the input string by 5 places in the alphabet, and the `decode_shift` function shifts every alphabetic character by 5 places back. The `% 26` operation ensures that the shift wraps around the alphabet.

The example usage at the end shows how to use these functions to encode and decode a string. The `isalpha()` method is used to check if a character is a letter before attempting to shift it, and the `lower()` method is used to convert the input string to lowercase to simplify the calculation.