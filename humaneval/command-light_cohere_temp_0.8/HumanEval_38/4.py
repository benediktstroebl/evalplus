Here is a Python script with a self-contained function that solves the problem of encoding and decoding markdown code:
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
    } part: each group of three characters contains a complete block, no need to decode further.
    return s.encode_cycl encoding
   
 original string.

This script provides a self-contained function that solves the problem of encoding and decoding markdown code using cyclic groups of three characters.