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
    + tests with test cases that passed for encode_cyclic function.
    """
    test_decode_cyclic(encode_cyclic("hello world")))
    test_enc("hello world", "hello world")
    test_enc("h e l l o w o rld ", "hello world")
    test_enc("^Apostrophe$", "hello world")
    test_enc("this is not valid encoded text", "this is not valid decoded text")
```
The function encode_cyclic splits the string into groups of length 3, cycles the characters in each group, and then joins the groups back together to form a string. The decode_cyclic function takes an string as input and returns the decoded version of that string.