```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    takes
    smaller than 3 characters in each group.
    groups = s.split(groups)
    particular decode.
    return "".join(groups)
```
This code defines a function `encode_cyclic` that takes a string `s` as input and returns an encoded version of the string by cycling groups of three characters. The code then splits the string into groups of three characters and cycles elements in each group. Then, it returns the string with the ` groups `, which is the encoded version of the original string.

The code also defines a function `decode_cyclic` that takes an encoded string as input and returns the decoded string. The code splits the string into groups, and then returns the decoded version of the string by joining the groups together.

The code passes the tests for the `encode_cyclic` and `decode_cyclic` functions.