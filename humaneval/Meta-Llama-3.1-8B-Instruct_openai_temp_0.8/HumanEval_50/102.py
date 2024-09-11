### Caesar Cipher Encoder & Decoder
#### Problem Statement: Implement a Caesar Cipher encoder and decoder in Python.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every lowercase character by 5 positions in the alphabet.

    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function and returns decoded string.

    :param s: Input string to be decoded.
    :return: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def main():
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")


if __name__ == "__main__":
    main()
```

#### Explanation:
*   We've implemented the `encode_shift` function to shift every lowercase character in the input string by 5 positions in the alphabet.
*   The `decode_shift` function reverses the encoding process by shifting the characters back by 5 positions.
*   Both functions use the modulo operator (`% 26`) to wrap around the alphabet if the shift exceeds 26.
*   We've added a condition (`if ch.isalpha()`) to only process alphabetical characters.
*   In the `main` function, we demonstrate the usage of the `encode_shift` and `decode_shift` functions with an example string.