```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by first subtracting the ASCII value of 'a' from each character in the string.
    This effectively gives us an index of the character in the alphabet (with 'a' being 0, 'b' being 1, etc.).
    We then add 5 to this index, wrap around to the start of the alphabet if necessary, and finally add back the ASCII value of 'a'.

    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by shifting every character back by 5 in the alphabet. This is done by subtracting 5 from each index (just like in the encode_shift function), and then converting the index back to a character.

    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    text = "hello"
    encoded_text = encode_shift(text)
    print(f"Encoded text: {encoded_text}")
    decoded_text = decode_shift(encoded_text)
    print(f"Decoded text: {decoded_text}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 places in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function reverses this process, shifting every character back by 5 places in the alphabet. Both functions work by first subtracting the ASCII value of 'a' from each character, then adjusting the index, and finally adding back the ASCII value of 'a' to get the decoded character. The example usage at the end shows how to use these functions to encode and decode a string.