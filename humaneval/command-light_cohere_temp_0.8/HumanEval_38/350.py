```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    expected
    drawback, does not handle all possible inputs, e.
    # int overflow. 
    if len(s) % 3 == 0: return s
    return decode_cyclic(s[3 * i:])
```

This Python script defines a self-contained function `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function is also defined to take an input string and return the decoded string.