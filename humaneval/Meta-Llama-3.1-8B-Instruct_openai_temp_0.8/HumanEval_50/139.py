### Shift Encoder and Decoder

Here's a self-contained Python script with the `encode_shift` and `decode_shift` functions. This script also includes a `main` function to demonstrate how to use these functions.

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 26 - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def main():
    # Example usage:
    original_string = "Hello World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

This script will encode the original string "Hello World!", then decode the encoded string, and finally print both the original and decoded strings. The code also includes input checking to ensure it only processes alphabetic characters.

The code uses the properties of modular arithmetic to simplify the shift operation. The expression `(ord(ch) - ord("a") + 5) % 26` shifts each character 5 positions forward in the alphabet, wrapping around from 'z' to 'a'. The `ord` function gets the ASCII value of a character, and `chr` gets the character represented by a specific ASCII value.

Note that the `if ch.isalpha()` condition is used to ignore non-alphabetic characters.