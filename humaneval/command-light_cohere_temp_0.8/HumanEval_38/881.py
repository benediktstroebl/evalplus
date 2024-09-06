Here's the self-contained Python function that solves the problem:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    Ul OH1, Ul Oh2, Ul Oh3 is a well-known mnemonic to remember the rule.
    """
    return s.replace(lambda x: x.replace(c, group[1] + group[0]) for c in s for group in groups)
```
This function takes a string s as input and returns the encoded version of the string, using the encoding technique described earlier. The decoding function is defined to take the encoded string as input and return the decoded string.