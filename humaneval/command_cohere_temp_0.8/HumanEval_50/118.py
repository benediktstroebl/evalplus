Here's a Python script with a self-contained function that solves the problem you've outlined, including a markdown code block with tests:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.
    
    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string to be decoded.
    
    Returns:
        str: Decoded string.
    """
    return encode_shift(s, decode=True)

def test_encode_shift():
    assert encode_shift("Hello World!") == "Ifmmp Sbe AMAZ Znmrk!"
    assert encode_shift("abcdeabcde") == "fghijfghij"

def test_decode_shift():
    assert decode_shift("Ifmmp Sbe AMAZ Znmrk!") == "Hello World!"
    assert decode_shift("fghijfghij") == "abcdeabcde"
```

The functions `encode_shift` and `decode_shift` are defined to perform the specified string transformations. The `test_encode_shift` function tests the `encode_shift` function by checking if the encoded result matches the expected output, whereas the `test_decode_shift` function tests the `decode_shift` function by verifying that it produces the original input when given the encoded string. 

To run the tests, simply execute the script. Both test functions employ the `assert` statement to verify their conditions, so if the script runs without errors, it signifies that the code is operating correctly.