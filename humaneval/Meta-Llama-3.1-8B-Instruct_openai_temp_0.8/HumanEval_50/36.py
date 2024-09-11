### Shift Encoding and Decoding Script
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to be decoded.
    :return: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script provides functions `encode_shift` and `decode_shift` to encode and decode strings by shifting every character by 5 in the alphabet. It also includes example usage in the `if __name__ == "__main__":` block to demonstrate the functionality. The script handles both lowercase and uppercase letters, leaving non-alphabet characters unchanged.