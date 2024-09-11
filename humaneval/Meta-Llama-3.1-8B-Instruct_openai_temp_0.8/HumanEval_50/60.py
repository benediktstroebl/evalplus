```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    # Test encode and decode functions
    encoded_str = encode_shift("hello world")
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions, `encode_shift` and `decode_shift`, which perform Caesar cipher encoding and decoding with a shift of 5. The `if __name__ == "__main__":` block provides an example usage of the functions. The `isalpha()` method is used to check if a character is a letter before applying the shift, and non-alphabetic characters are left unchanged.