```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    The function shifts each character in the input string by 5 places in the alphabet.
    It does this by first converting the character to its ASCII value, subtracting the ASCII value of 'a' to get a value between 0 and 25,
    adding 5, taking the modulus with 26 to ensure the value is still between 0 and 25,
    and then adding the ASCII value of 'a' to get the ASCII value of the shifted character.
    Finally, it converts the ASCII value back to a character and joins all the characters together into a string.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    The function does the opposite of encode_shift: it shifts each character back by 5 places in the alphabet.
    It does this by first converting the character to its ASCII value, subtracting the ASCII value of 'a' to get a value between 0 and 25,
    subtracting 5, taking the modulus with 26 to ensure the value is still between 0 and 25,
    and then adding the ASCII value of 'a' to get the ASCII value of the decoded character.
    Finally, it converts the ASCII value back to a character and joins all the characters together into a string.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    s = "hello"
    encoded = encode_shift(s)
    decoded = decode_shift(encoded)
    print(f"Original string: {s}")
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")
```

This script first defines the `encode_shift` and `decode_shift` functions as specified. Then, it includes an example usage at the end where it takes the string "hello", encodes it with `encode_shift`, decodes the encoded string with `decode_shift`, and prints the original string, encoded string, and decoded string.