Here's the solution to the markdown code block with the encode_cyclic and decode_cyclic functions:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g + g[::-1] for g in (g[1:] + g[0]) if len(g) == 3)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    plain groups have known to be decoded correctly.
    """
    return s.
"""