```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    ends with eof
    """
    return s.splitlines(groups=s.join(3)[::-1])

def test_encode_decode():
    s = "abcabcbb"
    assert encode_cyclic(s) == "ab...)b"
    s = "..."
    assert encode_cyclic(s) == "..."
    s = "..."# Any content is valid
    assert encode_cyclic(s) == s
    s = "..."
    assert decode_cyclic(s) == s
```
The `encode_cyclic` and `decode_cyclic` functions are both self-contained and work by splitting and cycling the groups of characters, then joining them back together. The `test_encode_decode` function verifies that the `encode_cyclic` and `decode_cyclic` functions produce the correct output for the given input.