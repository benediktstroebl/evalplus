```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    supports decoding of encode_cyclic
    """
    return s == encode_cyclic(s)
```

This Python script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. It achieves this by splitting the string into groups of three characters and then cycling elements within each group. The `decode_cyclic` function is used to test whether a given string has been correctly encoded using the `encode_cyclic` function.