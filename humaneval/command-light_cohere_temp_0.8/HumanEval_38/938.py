```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
     # return decoded string
    """
    return s.decode_cycl_cyclic("".decode_cyclic("XVdAeC"))  # Should return "abcdeABC"
```
This script defines a function encode_cyclic that converts a string into a markdown code block by cycling groups of three characters. The function also defines a decode_cyclic function, which takes an input string as decoded with the encode_cyclic function and returns the original decoded string.