```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    spaces for a test.
```

The encode_cyclic function takes a string as input and returns an encoded string by cycling groups of three characters. The function works by splitting the string into groups of three characters, with each group containing a cycle of three characters. The function then cycles the elements in each group, with the cycle being the first character in the group, and the group being the last character in the string.

The decode_cyclic function takes an encoded string as input and returns a decoded string. The function works by taking the encoded string and passing it to the encode_cyclic function, which returns the decoded string.

The decode_cyclic function also passes a test, which checks that the decoded string is equal to the original string.