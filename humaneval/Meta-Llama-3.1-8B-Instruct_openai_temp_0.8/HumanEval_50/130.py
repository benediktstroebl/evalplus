```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by first getting the ASCII value of each character.
    It then shifts each character by 5 in the alphabet by taking the modulus
    of 26 to ensure the result is within the range of 'a' to 'z'.
    Finally, it converts the result back to a character using chr().

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by first getting the ASCII value of each character.
    It then shifts each character by -5 in the alphabet by taking the modulus
    of 26 to ensure the result is within the range of 'a' to 'z'.
    Finally, it converts the result back to a character using chr().

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    # Test encode_shift function
    encoded_str = encode_shift("hello")
    print(f"Encoded string: {encoded_str}")

    # Test decode_shift function
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher for encoding and decoding strings, respectively. The `encode_shift` function shifts each character by 5 in the alphabet, and the `decode_shift` function shifts each character by -5 in the alphabet. The `if __name__ == "__main__":` block demonstrates the usage of these functions with example inputs.