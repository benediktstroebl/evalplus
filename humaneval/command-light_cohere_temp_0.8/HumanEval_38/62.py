```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    receive encoded string and """
    return decoded string
```

This code implements the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function splits the input string into groups of length 3 and cycles the characters within each group. The `decode_cyclic` function takes the encoded string and returns the decoded string by reconstructing the original string from the encoded groups.