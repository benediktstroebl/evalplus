```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of three characters.
    # cycle elements in each group of three characters
    groups = [list(c) for c in s[:3 * i] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    I test the the same text is to be decoded.
    if s == encode_cyclic('hello world'):
        print("pass")
    else:
        print("fail")
```