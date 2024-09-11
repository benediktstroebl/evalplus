```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    This function assumes that the input string contains only lowercase English letters.

    :param s: input string to be encoded
    :return: encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    This function assumes that the input string contains only lowercase English letters.

    :param s: input string to be decoded
    :return: decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this script, the `encode_shift` function shifts each character in the input string by 5 places in the alphabet, wrapping around the end of the alphabet if necessary. The `decode_shift` function reverses this process to get back the original string. The example usage demonstrates how to use these functions to encode and decode a string.