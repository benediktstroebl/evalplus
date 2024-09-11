```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5 + 26) % 26) + ord("a")) for ch in s])


# Test the functions
if __name__ == "__main__":
    s = "hello"
    encoded_s = encode_shift(s)
    print(f"Encoded string: {encoded_s}")

    decoded_s = decode_shift(encoded_s)
    print(f"Decoded string: {decoded_s}")
```

This script defines two functions, `encode_shift` and `decode_shift`, to perform Caesar cipher encoding and decoding. The encoding function shifts each character in the input string by 5 positions to the right in the alphabet, and the decoding function shifts each character back by 5 positions to the left. The script includes a test case to demonstrate the functions' behavior. I included the `ord("a")` in both functions and added a.lower() call to handle both uppercase and lowercase letters.