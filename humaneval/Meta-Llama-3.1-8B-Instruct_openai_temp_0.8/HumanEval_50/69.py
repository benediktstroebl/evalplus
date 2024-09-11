```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    The function works by first converting each character in the input string to its corresponding ASCII value.
    Then it shifts the value by 5 (wrapping around the alphabet if necessary) and converts it back to a character.
    Only lowercase letters are shifted, other characters (like uppercase letters, digits, and punctuation) are left unchanged.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works similarly to encode_shift, but instead of shifting the characters to the right, it shifts them to the left.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decode_shift(encoded_string)}")
```

Note that this code will only shift lowercase letters by 5 positions in the alphabet. If you want to shift both uppercase and lowercase letters, you will need to add additional logic to handle the case where `ch.isupper()`.