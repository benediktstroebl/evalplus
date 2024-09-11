```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function takes a string as input, shifts each lowercase character by 5 places 
    in the alphabet (wrapping around to the start of the alphabet if necessary), and returns 
    the encoded string. Non-alphabetic characters are not modified.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function takes a string as input, reverses the encoding done by encode_shift, 
    and returns the decoded string. Non-alphabetic characters are not modified.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts each lowercase alphabetic character in the input string by 5 places in the alphabet, wrapping around to the start of the alphabet if necessary. The `decode_shift` function reverses this encoding. The example usage at the end demonstrates how to use these functions.