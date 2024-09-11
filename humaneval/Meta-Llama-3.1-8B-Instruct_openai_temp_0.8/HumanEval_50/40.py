```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    The function works by converting each character in the string to its ASCII value,
    adding 5 (unless the character is a lowercase letter, in which case we remove
    the ASCII value of 'a' first, add 5, take the modulus 26, then add the ASCII
    value of 'a' back), and converting back to a character.

    :param s: The string to encode.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: The encoded string.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
input_string = "hello"
encoded_string = encode_shift(input_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input, shifts every letter by 5 positions in the alphabet, and returns the encoded string. The `decode_shift` function takes an encoded string as input and returns the original string by shifting every letter back by 5 positions in the alphabet.

Note that the script uses the `ord` function to get the ASCII value of characters, and the `chr` function to convert ASCII values back to characters. The `isalpha` function is used to check if a character is a letter, and the `islower` and `isupper` functions could be used to check if a character is a lowercase or uppercase letter respectively.

The example usage at the end shows how to use these functions to encode and decode a string.