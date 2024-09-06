```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    versions of a string.
    # reverse string
    version
    decoded version of encode_cyclic
    decoded = s.decode('utf-8-sig')
    return decoded

# test encode_cyclic function
def test_encode_cyclic():
    assert encode_cyclic("hello world") == "v3dlodrll"

# test decode_cyclic function
def test_decode_cyclic():
    assert decode_cyclic("v3dlodrll") == "hello world"
```

This script defines a self-contained function `encode_cyclic` that splits a given string into a list of groups of three characters each and cycles the characters in each group, and returns the list. The `decode_cyclic` function is also defined to reverse the encoding process and return the decoded string.

Finally, the script passes the test functions `test_encode_cyclic` and `test_decode_cyclic` to the respective functions to verify their correctness.