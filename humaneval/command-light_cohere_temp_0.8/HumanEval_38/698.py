```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [group[1:] + group[0]) if len(group) == 3 else group for group in s[:(len(s)+2)//3:]]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   1.
    Here is strings are encoded by encode_cyclic function.
    """
   
    """
    # split string to groups of length 3
    groups = [group[1:] + group[0]) if len(group) == 3 else group for group in s[:(len(s)+2)/3:]]
    return "".join(groups)
```