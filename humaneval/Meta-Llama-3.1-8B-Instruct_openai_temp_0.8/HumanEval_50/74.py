```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def test_functions():
    s = "Hello, World!"
    encoded = encode_shift(s)
    decoded = decode_shift(encoded)
    assert decoded == s, "Decoded string does not match original string"
    print("Test passed: Encoded and decoded strings match")


if __name__ == "__main__":
    test_functions()
```

In this code:

- The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet when reaching 'z' or 'Z'.
- The `decode_shift` function reverses the encoding process by shifting every character back by 5 positions in the alphabet.
- The `test_functions` function tests the correctness of the `encode_shift` and `decode_shift` functions by encoding and decoding a sample string, and asserting that the decoded string matches the original string.
- The script runs the `test_functions` function when executed directly.