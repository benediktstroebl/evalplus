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
    object that encode_cyclic string to match decoding.
```

The encode_cyclic and decode_cyclic functions take a string s as input and perform the encoding and decoding operations, respectively. They use a same self-contained approach to solve the problem. They split the string into groups of length 3 and cycle the characters in each group. The resulting encoded string is then returned.