```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function assumes the input string only contains lowercase English letters.

    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function assumes the input string only contains lowercase English letters.

    :param s: The input string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s])


# Test the functions
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines the `encode_shift` and `decode_shift` functions as specified. The `encode_shift` function shifts every character in the input string by 5 places in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function reverses this operation, effectively undoing the encoding.

The script also includes a test case that encodes the string "hello", decodes the result, and prints the original, encoded, and decoded strings.