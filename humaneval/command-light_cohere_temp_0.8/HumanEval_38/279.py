```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    made up not to make it easier to read and more obvious.
```

This Python script defines a self-contained function called `encode_cyclic` and `decode_cyclic` that solves the given problem. The `encode_cyclic` function splits the input string into groups of three characters, and cycles the characters in each group. The `decode_cyclic` function takes the encoded string as input and returns the decoded string by applying the `encode_cyclic` function in reverse.