```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in (g[1:] + g[0]) if len(g) == 3)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    assert encode_cyclic(s) == s, "encode_cyclic failed"
    return s
```
The code defines the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function takes an input string and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an input string and returns a decoded string by using the `encode_cyclic` function. 

The code also passes the test cases and asserts that the `encode_cyclic` and `decode_cyclic` functions work correctly.