### Shift Encoding and Decoding Script

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function shifts each character in the input string by 5 places in the alphabet.
    It presumes the input string only contains lowercase letters.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function shifts each character in the input string by 5 places back in the alphabet.
    It presumes the input string only contains lowercase letters.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s])


# Example usage
encoded_string = encode_shift("hello")
decoded_string = decode_shift(encoded_string)

print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

In the script, I made some improvements:

1.  The `ord(ch) - ord("a")` expression was used to convert the character to its corresponding position in the alphabet (from 0 to 25). This was then added to 5, and the result was taken modulo 26 to wrap around the alphabet if necessary.
2.  The `% 26` operation is used to ensure the shifted character's position in the alphabet is between 0 and 25. This prevents indices outside the valid range.
3.  I moved the code for encoding and decoding into separate functions for better organization and reusability.
4.  The example usage demonstrates how to use the `encode_shift` and `decode_shift` functions together to encode and then decode a string.