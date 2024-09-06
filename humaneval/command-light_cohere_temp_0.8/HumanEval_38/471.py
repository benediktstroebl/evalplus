```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    it
    returns decoded string
    """
    return s.decode_cycl_cyclic(s.encode_cyclic(s))
```

This Python script defines a self-contained function `encode_cyclic` that takes a string `s` as input and returns an encoded string by cycling groups of three characters. The function also defines a function `decode_cyclic` that takes an input string and returns its decoded version. The `decode_cyclic` function calls the `encode_cyclic` function with the input string, and returns the decoded result.