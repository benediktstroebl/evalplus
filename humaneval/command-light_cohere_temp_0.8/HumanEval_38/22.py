```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s if len(g) > 2 and g != ' ' and g[-1:]+=' ')


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    _ also decoded string, so this function passes the test.
```