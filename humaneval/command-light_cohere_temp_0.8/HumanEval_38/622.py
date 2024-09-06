```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g) for g in [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    at a!" reliever.
    encoded = encode_cyclic
   
    s = "abc".join(encoded)
    return s
```