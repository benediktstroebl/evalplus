```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    good strings that the first and last occurrences of non-alphine characters in the input.
    """
    return s.decode("{{encoded_string}}")
```

This script defines two self-contained functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function takes the encoded string as input and returns the decoded string by decoding the encoded string using the `encode_cyclic` function.