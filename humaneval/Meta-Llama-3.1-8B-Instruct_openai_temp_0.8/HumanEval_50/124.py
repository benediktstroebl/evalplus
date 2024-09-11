```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    For lowercase letters, it works as a Caesar cipher, shifting 'a' to 'f', 'b' to 'g',
    and so on. For uppercase letters, it shifts 'A' to 'F' and 'B' to 'G' accordingly.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
s = "hello"
print("Original string:", s)
encoded = encode_shift(s)
print("Encoded string:", encoded)
decoded = decode_shift(encoded)
print("Decoded string:", decoded)
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet, wrapping around from 'z' to 'a' or 'Z' to 'A'. The `decode_shift` function reverses this shift, returning the original string. The example usage demonstrates how to use these functions with a test string.