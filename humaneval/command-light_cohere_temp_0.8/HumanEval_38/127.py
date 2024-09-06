Here's the solution to the markdown encoding problem:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [sub for sub in s[::3]]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    goods(encoded string)"""
    return encode_cyclic(s)

# test cases
def test_encode_cyclic():
    assert encode_cyclic("Hello World!") == "H@#$oW"

def test_decode_cyclic():
    assert decode_cyclic("H@#$oW") == "Hello World!"
```

This code defines the `encode_cyclic` and `decode_cyclic` functions, which are used to encode and decode markdown-like strings using a cyclic group of three characters. The `test_encode_cyclic` and `test_decode_cyclic` functions are used to verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.