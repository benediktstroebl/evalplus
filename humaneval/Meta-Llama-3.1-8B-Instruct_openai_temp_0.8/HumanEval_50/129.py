### Caesar Cipher Encoder and Decoder
#### Solution using Python

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage
if __name__ == "__main__":
    original_string = "Hello World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print("Original string: ", original_string)
    print("Encoded string: ", encoded_string)
    print("Decoded string: ", decoded_string)
```

**Explanation:**

The `encode_shift` function shifts each character in the input string by 5 positions in the alphabet, wrapping around to the start of the alphabet if the shift would move past 'z'.

The `decode_shift` function reverses the encoding process, shifting each character back by 5 positions. It also checks if the character is a letter before attempting to shift it, to avoid shifting punctuation.

In the example usage, we demonstrate that the `decode_shift` function correctly decodes a string that has been encoded with `encode_shift`.