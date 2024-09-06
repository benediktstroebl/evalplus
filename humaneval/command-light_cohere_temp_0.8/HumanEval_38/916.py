```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    read-only.
    """
    read-only string that is encoded.
"""

def test_encode_decode():
    """
    checks encode and decode function
    """
    s = "abc"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert encoded == decoded
    s = "aaaaaa"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert decoded == s
    s = "aaabaaa"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert decoded == s

test_encode_decode()
```
This script defines a function encode_cyclic which splits a string into groups of length 3, and cycles the first character of each group, and returns an encoded string. The function also handles the decode_cyclic which takes an encoded string, and returns the decoded string. The test_encode_decode function contains test cases for the encode_cyclic and decode_cyclic functions, which check if the functions return the correct decoded string.