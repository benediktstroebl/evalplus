```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    read as a plain text, but "decoded" will have the encoding.
    """
    return s
return "Decoded text"
```
This code contains two self-contained functions:
1. `encode_cyclic(s: str) -> str`: This function encodes a given string by cycling groups of three characters. It does this by splitting the string into groups of three characters, and then cycling the first character of each group.
2. `decode_cyclcyclic(s: str) -> str`: This function decodes a given string that was encoded using the encode_cyclic function. It returns the string, which in this case is the decoded text.