```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to encode
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to decode
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def main():
    # Example usage
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

This script defines two functions, `encode_shift` and `decode_shift`, which perform the required operations. The `encode_shift` function shifts each lowercase alphabetic character in the input string by 5 positions in the alphabet, while the `decode_shift` function does the reverse to restore the original string. The `main` function demonstrates how to use these functions with an example string.