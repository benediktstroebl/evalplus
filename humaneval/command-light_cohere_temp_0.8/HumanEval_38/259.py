```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    done by calling each group back to its original string.
    return "".join(g[::-1]) if g else "".join([])
```
This code defines a function that takes a string as input and returns an encoded version of the string by cycling groups of three characters. It also defines a string-passing functions for both encode and decode operations.