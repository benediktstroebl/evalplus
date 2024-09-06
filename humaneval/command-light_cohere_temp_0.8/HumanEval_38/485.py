```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [sub for sub in s if len(sub) == 3]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    might need only be decoded to the original string.
```
This code defines a function encode_cyclic that takes a string s and returns a string with each group of three characters separated by spaces. The function then defines a second function decode_cyclic that takes a string encoded with the encode_cyclic function and returns the original string.