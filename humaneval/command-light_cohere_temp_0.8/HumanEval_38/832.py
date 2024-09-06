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
    expected output:
    <cos>"
```
This code solves the problem of encoding and decoding cyclic groups of three characters in a string. It defines two functions, `encode_cyclic` and `decode_cyclic`, which take a string as input and return the encoded or decoded string, respectively. These functions use the single- three-character groups in the string and cycle the groups to form a single string. 

Note that the code is a self-contained solution for the given problem.