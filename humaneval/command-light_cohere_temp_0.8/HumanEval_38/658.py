```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    number of cases, these are the same """
    return encode_cyclic(s) == s

# test cases
assertEqual(encode_cyclic("abc"), "abc")
assertEqual(encode_cyclic("abcd"), "abcd")
assertEqual(encode_cyclic("abdec"), "aced")
assertEqual(encode_cyclic("aedc"),"ade")
assertEqual(encode_cyclic("ace"),"ac")

# these are different!
assertEqual(encode_cyclic("ace"), "ac")

```