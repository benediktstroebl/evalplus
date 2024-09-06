```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(x for x in s if len(x) == 3)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
     ... If the input string is encoded with a group of three characters, return decoded string.
    """
    test: assert encode_cyclic("hello") == "oi"
    """
    return s

```