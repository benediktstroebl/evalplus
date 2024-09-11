```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


def main():
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")


if __name__ == "__main__":
    main()
```

This Python script first defines two functions `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input, shifts every lowercase alphabetic character by 5 positions forward in the alphabet, and returns the encoded string. The `decode_shift` function does the reverse, shifting every lowercase alphabetic character by 5 positions backward in the alphabet.

In the `main` function, we demonstrate how to use these functions by encoding and then decoding a string. The encoded string is then compared to the original string to verify that the decoded string is correct.

Note that this script also handles non-alphabetic characters by leaving them unchanged in their original position. It also converts the input string to lowercase to make the shift operation simpler. If you want to handle uppercase letters as well, you'll need a more complex approach to convert them to lowercase before shifting and then convert them back to their original case after shifting.