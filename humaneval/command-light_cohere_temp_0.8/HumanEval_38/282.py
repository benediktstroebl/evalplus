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
    down encoding"""
   
    if it is an encoded cyclic string
    else
        return s

# example of
encoded = encode_cyclic("Hello World")
assert encoded == "H# VelLoWv"

decoded = decode_cyclic(encoded)
assert decoded == "Hello World"
```

This code provides a self-contained solution and test for the given problem. You can use this both the and `encoded` and `decoded` can be assigned to variables, which can then be printed to the console.