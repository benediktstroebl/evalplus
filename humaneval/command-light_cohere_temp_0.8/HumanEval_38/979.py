```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    sure to pass test the
    it's encoded with encode_cyclic function
    """
    return encode_cyclic(s)

def test_encode_decode():
    """
    tests the encode_cyclic and decode_cyclic functions
    """
    s = "abc123"
    assert encode_cyclic(s) == "a123b123"
    s = " ABCABCABC"
    assert encode_cyclic(s) == "a123b123"
    s = "abc"
    assert encode_cyclic(s) == "ab"
    s = "abc" * 1000
    assert encode_cyclic(s) == "".join("abc" for i in range(1000))
    s = "1234"
    assert decode_cyclic(s) == s
    s = "12345"
    assert decode_cyclic(s) == s

test_encode_decode()
```
This Python script defines a self-contained function that solves the problem of encoding and decoding cyclic groups of characters. It also includes a test case to validate the functions.