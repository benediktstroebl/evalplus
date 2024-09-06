Here's a Python script with a self-contained function that solves the problem you've described, along with a script to decode the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes the input string by shifting each character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.
    
    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes an input string encoded with the encode_shift function.
    
    Args:
        s (str): Input string to be decoded.
    
    Returns:
        str: Decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])

# Unit tests:
def test_encode_shift():
    assert encode_shift("hello") == "ifmmp"
    assert encode_shift("world") == "zdncw"

def test_decode_shift():
    assert decode_shift("ifmmp") == "hello"
    assert decode_shift("zdncw") == "world"

test_encode_shift()
test_decode_shift()
```

This script defines the two functions `encode_shift` and `decode_shift` as described in the prompt. It also provides two unit tests, `test_encode_shift` and `test_decode_shift`, to ensure that the functions produce the expected results.

The `encode_shift` function encodes a string by shifting each character by 5 in the alphabet. It iterates over each character in the input string, calculates the new ordinal value of the character after applying the shift, and then converts it back to a character within the ASCII range. The `decode_shift` function decodes an encoded string by reversing the shift operation. It shifts each character back by 5 to recover the original string.

The unit tests check the functionality of the encode and decode functions by comparing the encoded and decoded strings for various input messages.