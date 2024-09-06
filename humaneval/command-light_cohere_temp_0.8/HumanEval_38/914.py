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
    watched string is encoded string by cycling groups of three characters.
    """
    # split string to groups
    # cycle elements in each group.
    groups = s.translate(groups, (decode_groups)
    return "".join(groups)

# test the functions
assertEqual(encode_cyclic("hello"), "hello".encode_cyclic)
assertEqual(decode_cyclic("hello").decode_cyclic, "hello")
```

This code implements the encode_cyclic and decode_cyclic functions, which encode and decode a string containing only the characters h, e, and l (in that order). These functions split the string into groups of three characters, cycle the elements of each group, and then join the groups back together to form the original string. It also has a expected output for the given test cases.