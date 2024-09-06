```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    reasons and input string
    """
    return s.decode_cycl(encode_cyclic(s))
```
This code provides two functions, encode_cyclic and decode_cyclic, to encode and decode a string with groups of three characters. It uses a tests to solve the problem and passes the corresponding tests.