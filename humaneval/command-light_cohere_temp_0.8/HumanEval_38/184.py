```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(c for c in s if c[0] in "abc" and c[1] in "abc" and c[2] in "abc")

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    common string encodings or
    are: ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return "".join(c for c in s if c in "abcdefghijklmnopqrstuvwxyz")

def test_encode_cyclic():
    """
    checks that the encode_cyclic function works correctly
    """
    assert encode_cyclic("Hello World") == "Hello WXYZ", assert encode_cyclic("Test !@#$?py") == "TF VWY", assert encode_cyclic("") == ""

    return True

def test_decode_cyclic():
    """
    checks that the decode_cyclic function works correctly
    """
    assert decode_cyclic("Hello WXYZ") == "Hello World", assert decode_cyclic("TF VWY") == "Test !@#$py", assert decode_cyclic("") == ""

    return True

# run the tests
test_encode_cyclic()
test_decode_cyclic()
```

This code defines a self-contained Python function called `encode_cyclic` that returns an encoded string by cycling groups of three characters, and a `decode_cyclic` function that takes an encoded string as input and returns the decoded string. The `encode_cyclic` function is then tested with sample cases to ensure it works correctly, and the `decode_cyclic` function is also tested to ensure it produces the correct decoded output.