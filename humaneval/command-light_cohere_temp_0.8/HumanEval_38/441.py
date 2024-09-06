Here is a Python script that defines a self-contained function that solves the problem of encoding and decoding markdown code:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    returns decoded string
    decoded = s.split('..join([group[1:] + group[0]) if len(group) == 3 else group for group in s.split(''.join(groups))
    return ''.join(decoded)
```

This script defines a function encode_cyclic that takes a string s as input and returns a string where each group of three characters is joined together with an enclosing space, resulting in a properly encoded string. The function also defines a decode_cyclic function, which takes an input string s and returns the decoded version of the string. The decode_cyclic function splits the input string into a list of lists of characters, and then joins the lists back together into a single string, which is the decoded version of the input.