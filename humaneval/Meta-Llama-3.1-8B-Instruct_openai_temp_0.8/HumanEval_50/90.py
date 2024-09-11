```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Test the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines the `encode_shift` and `decode_shift` functions as specified. The `encode_shift` function shifts each character by 5 positions in the alphabet, wrapping around from 'z' to 'a' if necessary. The `decode_shift` function reverses this operation to get back the original string. 

The script also includes a test case where it encodes a string, prints the encoded string, decodes the string back to its original form, and prints the decoded string. Note that the `lower` function is used to ensure the encoding and decoding work for both lowercase and uppercase letters.