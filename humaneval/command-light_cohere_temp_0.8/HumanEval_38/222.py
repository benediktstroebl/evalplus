```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[::-1] for g in ((g for g in s if len(g) > 2 and g != '').join(' ' ')))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    simulates the ATMOSP character of the given string.
```

This Python script defines a self-contained function `encode_cyclic` that takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes the input string as well and returns the decoded string, simulating the behavior of an ATMOS patent.