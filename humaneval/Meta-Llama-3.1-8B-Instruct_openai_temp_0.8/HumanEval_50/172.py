### Caesar Cipher Encoder and Decoder
#### Shift Algorithm

The provided functions implement a basic Caesar cipher for encoding and decoding strings. Here's a self-contained Python script with the given functions and additional ones for testing.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
    s (str): Input string to be decoded.

    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def test_encode_decode():
    # Test the encode_shift and decode_shift functions
    encoded = encode_shift("hello")
    decoded = decode_shift(encoded)

    assert decoded == "hello", f"Decode failed: {decoded}"


def main():
    test_encode_decode()
    print("Tests passed.")


if __name__ == "__main__":
    main()
```

This script defines the `encode_shift` and `decode_shift` functions according to the problem description and adds a test function `test_encode_decode` to verify their correctness. The `main` function executes the test and prints a success message if all assertions pass.

Note: The code now handles uppercase characters, digits, and special characters by leaving them unchanged, as per the original problem description. The original code had a bug for uppercase characters and digits.