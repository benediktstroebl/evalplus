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
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    goals:
    test if the string decoded correctly.
    return True.eq(s) == decode_cyclic(s))
```

This Python code implements a self-contained function, `encode_cyclic`, which takes a string as input and encodes it by cycling groups of three characters. The `decode_cyclic` function is used to test the decoded string, and returns True if the decoded string matches the output of `encode_cyclic`. This code is designed to be self-contained, meaning it can be split into smaller functions and still be tested as a whole.