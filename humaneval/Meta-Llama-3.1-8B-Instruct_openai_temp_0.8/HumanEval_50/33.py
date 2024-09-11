```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 25 - 5) % 26) + ord("a")) for ch in s])


def main():
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

In this code:

- The `encode_shift` function shifts every character in the input string `s` by 5 places in the alphabet. It uses the ASCII values of characters to perform this shift. The expression `ord(ch) - ord("a")` calculates the position of the character in the alphabet (0 for 'a', 1 for 'b', etc.). Adding 5 to this position and taking the modulus by 26 (the number of letters in the alphabet) gives the new position. We then add `ord("a")` to get the ASCII value of the encoded character, and use `chr` to convert this back to a character.

- The `decode_shift` function reverses the encoding process by subtracting 5 from the position of each character in the alphabet.

- The `main` function demonstrates how to use these functions. It encodes the string "hello world", prints the encoded string, decodes it, and prints the decoded string.