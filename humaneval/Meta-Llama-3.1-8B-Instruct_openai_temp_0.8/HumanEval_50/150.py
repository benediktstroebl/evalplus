### Shift Encoding/Decoding Script

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input encoded string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
input_string = "Hello, World!"
encoded_string = encode_shift(input_string)
decoded_string = decode_shift(encoded_string)

print(f"Input String: {input_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

This script uses the `ord()` function to get the ASCII value of characters and the `chr()` function to get the character represented by a specific ASCII value. It also utilizes the modulo operator (`%`) to handle characters that are shifted beyond the alphabet.

In the `encode_shift()` function, we shift each character in the string by 5 positions in the alphabet. If the character is not a letter (i.e., it is a space, punctuation, etc.), we leave it unchanged.

In the `decode_shift()` function, we shift each encoded character back by 5 positions in the alphabet to retrieve the original string.

Note that this script converts the input string to lowercase before encoding/decoding it. If you want to preserve the original case, you can remove the `.lower()` method calls.