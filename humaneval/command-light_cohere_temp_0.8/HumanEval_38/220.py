```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   DOCUMENTED DECODE FUNCTION
    """
    return s.decode("".aaccc"
```
This code defines two functions, `encode_cyclic` and `decode_cyclic`, which respectively encode and decode markdown code blocks. The `encode_cyclic` function splits the input string into groups of three characters, and then cycles the characters within each group. The `decode_cyclic` function takes an encoded string and returns the decoded version of the input.

The `decode_cyclic` function uses the `decode` function from the string to return the decoded version of the input string.