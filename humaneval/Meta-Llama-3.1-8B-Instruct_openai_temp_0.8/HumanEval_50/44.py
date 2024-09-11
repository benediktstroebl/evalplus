```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function is case-sensitive, meaning it will treat lowercase and uppercase letters as separate characters.
    It also preserves the original casing of the input string.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works similarly to encode_shift, but shifts the characters in the opposite direction.

    :param s: Input string to be decoded
    :return: Decoded string
    """
    shift = -5
    return "".join([chr(((ord(ch) - ord("a") + shift) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
encoded_str = encode_shift("Hello, World!")
print("Encoded string:", encoded_str)

decoded_str = decode_shift(encoded_str)
print("Decoded string:", decoded_str)
```

This script defines the `encode_shift` and `decode_shift` functions as described, and provides an example usage at the end. The `encode_shift` function shifts every alphabetical character in the input string by 5 positions in the alphabet, preserving the original casing. The `decode_shift` function reverses the encoding by shifting the characters in the opposite direction. Both functions handle non-alphabetical characters (such as spaces and punctuation) by leaving them unchanged.