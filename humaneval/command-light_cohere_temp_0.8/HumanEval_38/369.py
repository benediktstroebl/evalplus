Here is a Python script that includes a self-contained function that solves the problem:
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
   - encoding comes To use encode_cyclic function
    """
    return encode_cyclic(s)

def test_encode_decode():
    """
    tests the encode_cyclic function
    """
    assert encode_cyclic("hello") == "..."
    assert encode_cyclic("world") == "..---"
    assert encode_cyclic("hello world") == "..." .---."
    assert encode_cyclic("hello world ") == "..." .---."-"
    assert encode_cyclic("") == ""
    assert encode_cyclic("  ") == ""
    assert encode_cyclic("  ____ ") == ".__---."
    assert encode_cyclic("a b  ") == "a---b"
    assert encode_cyclic("  _  ") == "  _   "
    assert encode_cyclic("hello , world ") == "..." .---."---
    assert encode_cyclic("  ,  ") == "..." .---.

test_encode_decode()
```

This script provides a self-contained function for encoding and decoding markdown code using the `encode_cyclic` and `decode_cyclic` functions. The test_encode_decode function verifies the functionality of the `encode_cyclic` function with various test cases.