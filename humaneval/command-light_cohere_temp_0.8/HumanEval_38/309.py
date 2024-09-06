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
    takes as input string encoded with encode_cyclic function. Returns decoded string
    partners in groups of three-character strings, each starting with a period.
    """
    return s.decode(encode_cyclic(s))
```

This Python script defines a self-contained function that solves the given problem. The function `encode_cyclic` encodes a given string by cycling groups of three characters. The function `decode_cyclic` takes an input string and returns its decoded string by using the `encode_cyclic` function.