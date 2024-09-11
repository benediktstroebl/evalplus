### Shift Encoder and Decoder

This script provides a simple implementation of a Caesar cipher for encoding and decoding strings.

```python
def encode_shift(s: str) -> str:
    """
    Encodes every character in the input string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha() and ch.islower()])

def decode_shift(s: str) -> str:
    """
    Decodes the input string, which is assumed to be encoded with encode_shift function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha() and ch.islower()])


def main():
    # Test the functions
    test_string = "abcde"
    encoded_string = encode_shift(test_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

### Explanation

*   The `encode_shift` function shifts every lowercase letter in the input string by 5 positions forward in the alphabet.
*   The `decode_shift` function shifts every lowercase letter in the input string by 5 positions backward in the alphabet to reverse the encoding.
*   The `main` function is used to test the functions with a sample string.
*   The `if __name__ == "__main__":` block ensures the `main` function is only executed when the script is run directly, not when it's imported as a module.

Note that the script checks if each character is a lowercase letter to avoid shifting non-alphabet characters. You may modify the script to handle uppercase letters or other characters as needed.