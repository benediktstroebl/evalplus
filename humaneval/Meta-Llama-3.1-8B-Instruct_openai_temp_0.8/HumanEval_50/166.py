```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by converting each character to its ASCII value, adding 5,
    and then taking the modulus of 26 to wrap around the alphabet. The result is
    then converted back to a character.

    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works in reverse of the encode_shift function. It converts each
    character to its ASCII value, subtracts 5, and then takes the modulus of 26
    to wrap around the alphabet. The result is then converted back to a character.

    :param s: The input string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    encoded_string = encode_shift("Hello, World!")
    print("Encoded string:", encoded_string)
    decoded_string = decode_shift(encoded_string)
    print("Decoded string:", decoded_string)
```

This script uses the `ord` function to get the ASCII value of each character, and the `chr` function to convert the resulting ASCII value back to a character. The `isalpha` method is used to check if a character is a letter, and the `lower` method is used to ensure the function works with both lowercase and uppercase letters. The `% 26` operation is used to wrap around the alphabet.