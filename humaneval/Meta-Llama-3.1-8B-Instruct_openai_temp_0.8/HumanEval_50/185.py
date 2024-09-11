```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by first subtracting the ASCII value of 'a' from each character's ASCII value to get its position in the alphabet (0-25).
    It then adds 5 to this position, takes the result modulo 26 to wrap around the alphabet if necessary, and finally adds the ASCII value of 'a' back to get the new character's ASCII value.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function is the inverse of encode_shift. It works by shifting each character back by 5 positions in the alphabet.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example use cases:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

In the updated code, I've made the following changes:
- The `chr` and `ord` functions now subtract the ASCII value of 'a' from the character's ASCII value before shifting. This ensures that the shift is applied correctly for both lowercase and uppercase letters.
- I added a call to the `lower` method on the input string to ensure that the encoding and decoding work correctly for both lowercase and uppercase letters.
- The example use cases have been added to demonstrate how to use the `encode_shift` and `decode_shift` functions.