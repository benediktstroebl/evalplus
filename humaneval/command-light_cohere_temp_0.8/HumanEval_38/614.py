```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    _ _ simple string like to solve the problem.
```
The `encode_cyclic` and `decode_cyclic` functions are self-contained. They split a string into groups of three characters, and then cycle elements in each group. The output is the decoded string.