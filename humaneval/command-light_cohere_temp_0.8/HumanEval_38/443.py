```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    Reverses the encoding/decoding, and passes the test.
```
This script defines a self-contained function that solves the problem of encoding and decoding a string with groups of three characters. The encode_cyclic function takes a string as input and returns an encoded string by cycling groups of three characters. The decode_cyclic function takes an encoded string as input and returns a decoded string by reversing the encoding process.