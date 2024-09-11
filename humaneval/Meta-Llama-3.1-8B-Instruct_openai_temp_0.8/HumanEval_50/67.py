```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    This function works by converting every character in the string to its corresponding
    ASCII value, adding 5 to it, taking the modulus with 26 (the number of alphabets),
    and then converting the result back to a character.

    Parameters:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by shifting every character in the input string in reverse
    direction by 5.

    Parameters:
    s (str): Input string to be decoded.

    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

In this script, the `encode_shift` function takes a string as input, shifts every lowercase alphabet in the string by 5 places to the right, and returns the encoded string. The `decode_shift` function takes the encoded string as input, shifts every lowercase alphabet in the string by 5 places to the left, and returns the decoded string. The example usage at the end demonstrates how to use these functions.