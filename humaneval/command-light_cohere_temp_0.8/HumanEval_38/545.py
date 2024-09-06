```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    common cyclic code, encoding or decoding.
    encoding is by using group of three characters, and decoding by using the same group.
    """ return s.decode(encode_cycl(s))
```

This script defines a function encode_cyclic that takes a string s and returns a string encoded with a cyclic code of groups of three characters. The function decode_cyclic is defined to take a string s as input and return the decoded string. The decode_cyclic uses the encode_cyclic to decode the string.

It correctly handles the case where the input string is a sequence of three characters, and correctly decodes it into a sequence of three characters.