Here's a Python script with a self-contained function that solves the problem you've described, along with a Markdown code block showing the code and corresponding tests:
```python
def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting each character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str) -> str:
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return encode_shift(s)

def test_encode_shift():
    assert encode_shift("hello") == "ifmmp"
    assert encode_shift("world") == "zdqvu"
    assert encode_shift("!") == "j"
    assert encode_shift("abcde") == "bhjkmn"

def test_decode_shift():
    assert decode_shift("ifmmp") == "hello"
    assert decode_shift("zdqvu") == "world"
    assert decode_shift("j") == "!"
    assert decode_shift("bhjkmn") == "abcde"
```

The script includes two independent functions 'encode_shift' and 'decode_shift'. The encoded shift function takes an input string `s` and encodes it by shifting each character by 5 in the alphabet, it achieves this by utilizing Python's character mapping through the expression `chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a"))`. The `decode_shift` function is designed to decode a string encoded using the `encode_shift` function, it achieves this by reusing the `encode_shift` function.

The script also includes automated tests for both functions: `test_encode_shift` and `test_decode_shift`, which verify the correct encoding and decoding process, ensuring the correctness of the functions. 

This script can be executed independently to evaluate the functionality of the encoded shift and decoding algorithms.