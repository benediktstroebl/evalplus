### Caesar Cipher Encoder and Decoder

This script includes two functions: `encode_shift` and `decode_shift`. They are used to encode and decode strings using the Caesar Cipher method.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
    s (str): The string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
    s (str): The string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script includes necessary error handling for non-alphabetical characters by keeping them unchanged during encoding and decoding. The `isalpha()` method checks whether a character is a letter, and `lower()` function is used to handle both lowercase and uppercase letters.