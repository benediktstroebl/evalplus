```python
def encode_shift(s: str):
    """
    Returns an encoded string by shifting every character by 5 in the alphabet.

    :param s: The input string to be encoded
    :return: The encoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: The input string to be decoded
    :return: The decoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


def main():
    # Example usage
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

This script provides two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 places in the alphabet, wrapping around to the beginning of the alphabet when it reaches the end. The `decode_shift` function reverses this encoding by shifting the characters back by 5 places.

The `main` function demonstrates how to use these functions with an example string "hello". The encoded string is printed to the console, and then the decoded string is printed to the console, showing that the original string is recovered.