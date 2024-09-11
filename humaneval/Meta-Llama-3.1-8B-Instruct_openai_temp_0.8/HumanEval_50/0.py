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
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Testing the functions
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This script first defines the `encode_shift` and `decode_shift` functions. The `encode_shift` function shifts each character in the input string to the right by 5 positions in the alphabet, wrapping around to the beginning of the alphabet when necessary. The `decode_shift` function reverses the shift, moving each character 5 positions to the left.

In the `if __name__ == "__main__":` block, the script tests these functions by encoding and then decoding the string `"hello"`. It then prints the original string, the encoded string, and the decoded string to verify that they match the original string. 

Note: The script uses the `lower()` method to convert all characters in the input string to lowercase, since the shift operation is designed to work with lowercase letters.