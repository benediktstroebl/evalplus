```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    
    same string is encoded with encode_cyclic function.
    return s
```
This code defines a function called **encode_cyclic** which accepts a string and returns the encoded version of the string. It also defines a function called **decode_cyclic** which accepts an string and returns the decoded version of the string, which is the original string with backslashes the **encode_cyclic** function.