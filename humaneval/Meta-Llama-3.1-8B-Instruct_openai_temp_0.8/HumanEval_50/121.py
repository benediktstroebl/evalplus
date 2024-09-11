```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    The function assumes the input string only contains lowercase letters.
    It shifts each letter to the right by 5 places in the alphabet, wrapping around to the start of the alphabet if necessary.

    Parameters:
        s (str): The string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    The function assumes the input string only contains lowercase letters.
    It shifts each letter to the left by 5 places in the alphabet, wrapping around to the end of the alphabet if necessary.

    Parameters:
        s (str): The string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Example usage:
original_string = "abcde"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original string: {original_string}")
print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

In this script, the `encode_shift` function takes a string `s` as input and returns a new string where each character has been shifted 5 places to the right in the alphabet. The `decode_shift` function does the opposite, taking an encoded string as input and returning the original string.

Note that both functions assume the input strings only contain lowercase letters. If the input strings can contain uppercase letters or other characters, the functions may need to be modified accordingly.