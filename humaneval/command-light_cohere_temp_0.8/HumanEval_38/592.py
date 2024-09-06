```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    splits the string into groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    Ever had to change between encoding and decoding, the function is helpful.
```
This script contains a self-contained function, encode_cyclic, which encodes a given string by cycling groups of three characters. It then splits theever the original string into groups of three characters, and then cycles the elements in each group. The function also ensures that each group has at least three characters. The function then returns the unencoded string.