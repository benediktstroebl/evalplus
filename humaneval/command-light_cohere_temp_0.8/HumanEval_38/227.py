```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
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
    str substring to get from from the input string
    and perform decoding.
    The original string is returned.
```

This script defines a self-contained function, `encode_cyclic`, that performs the encoding operation and returns the encoded string. The function also defines a second function, `decode_cyclic`, that takes the encoded string as input and returns the original decoded string.