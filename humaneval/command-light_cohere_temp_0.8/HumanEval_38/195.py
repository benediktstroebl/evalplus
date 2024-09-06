```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(groups)
    
def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
     and passes all tests.
    assert encode_cyclic(decode_cyclic(s)), "Should get original string back.")
```