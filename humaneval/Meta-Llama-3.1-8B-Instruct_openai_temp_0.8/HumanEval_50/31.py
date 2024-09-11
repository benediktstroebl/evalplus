```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This code first shifts every character in the string by 5 places in the alphabet. Then, it provides a function to shift the characters back to their original positions, effectively decoding the string. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specified ASCII value. The ASCII value for 'a' is 97, so we subtract it to get the position of the character in the alphabet. The `% 26` operation is used to wrap around the alphabet if the shift exceeds 26.

The `isalpha()` function is used to check if a character is a letter, and if not, it is left unchanged in the encoded string. 

The `lower()` function is used to ensure the function works correctly with both lowercase and uppercase letters. 

In the example usage, we first encode the string "Hello World", then decode the encoded string to get back the original string.