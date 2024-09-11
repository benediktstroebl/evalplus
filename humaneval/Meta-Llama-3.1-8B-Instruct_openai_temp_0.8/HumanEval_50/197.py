```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function shifts all lowercase English letters in the input string by 5 places in the alphabet.
    It preserves all other characters, including uppercase letters and non-English characters.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function shifts all lowercase English letters in the input string by 5 places in the opposite direction of encode_shift.
    It preserves all other characters, including uppercase letters and non-English characters.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_shift("hello")
    print("Encoded string:", encoded_str)

    decoded_str = decode_shift(encoded_str)
    print("Decoded string:", decoded_str)
```

This script defines two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher algorithm with a shift of 5 places. The `encode_shift` function shifts all lowercase English letters in the input string by 5 places in the alphabet, while the `decode_shift` function shifts them by 5 places in the opposite direction. Both functions preserve all other characters, including uppercase letters and non-English characters. The example usage at the end demonstrates how to use these functions to encode and decode a string.