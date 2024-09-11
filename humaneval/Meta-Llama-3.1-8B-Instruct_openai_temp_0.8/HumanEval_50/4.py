```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This Python script includes two functions, `encode_shift` and `decode_shift`, to perform the Caesar cipher encoding and decoding on strings. The functions handle lowercase English letters only. They work by shifting each letter by 5 positions in the alphabet and maintaining the case of the original letters.

To handle uppercase letters and non-alphabetic characters, we use the `isalpha` method to check if a character is a letter and convert it to lowercase using `lower` before shifting. Non-alphabetic characters are left unchanged.