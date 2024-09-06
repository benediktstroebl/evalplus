```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    quality-decoding can group-based cyclic encoding"""
    return s.decode(''.CRLF')


def test_encode_cyclic():
    s = "grape123 , apple Macy car"
    encoded = encode_cyclic(s)
    assert encoded == "123,acgr"


def test_decode_cyclic():
    s = "123, acgr"
    decoded = decode_cyclic(s)
    assert decoded == "grape123 , apple Macy car"
```
This code defines two functions, `encode_cyclic` and `decode_cyclic`, that perform cyclic encoding and decoding on a string. The `test_encode_cyclic` and `test_decode_cyclic` functions have test cases that verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.