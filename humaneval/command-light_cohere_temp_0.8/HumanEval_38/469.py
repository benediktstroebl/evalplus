Here's the Python code:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    both encoding and decoding function."""
    return s.encode_cycl_cyclic(s)

def test_encode_decode():
    """
    test cases for encoding and decoding functions."""
    assert encode_cyclic("test") == decode_cyclic("test")
    assert encode_cyclic("abc") == decode_cyclic("abc")
    assert encode_cyclic("abcd") == decode_cyclic("abcd")
    assert encode_cyclic("abcde") == decode_cyclic("abcde")
    assert encode_cyclic("abcdef") == decode_cyclic("abcdef")
    assert encode_cyclic("") == decode_cyclic("")

if __name__ == "__main__":
    test_encode_decode()
```

This script contains the functions **encode_cyclic** and **decode_cyclic**, which encode and decode markdown codes. The **test_encode_decode** function contains a set of test cases for both functions to verify their correctness.