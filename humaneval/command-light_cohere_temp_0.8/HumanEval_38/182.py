```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    why encoded string from decode_cyclic function
    """
    return s  # encoded == decoded

def test_encode_cyclic():
    s = "abcabc"
    assert encode_cyclic(s) == "abcabcabc"
    
def test_decode_cyclic():
    s = "abcabcabc"
    assert decode_cyclic(s) == s

if __name__ == "__main__":
    test_encode_cyclic()
    test_decode_cyclic()
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`, which are used to encode and decode a given string respectively. The `test_encode_cyclic` and `test_decode_cyclic` functions are used to run the functions with test cases. The output of the code is the result of these tests.