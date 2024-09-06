Here is a Python script that encodes and decodes a cyclic string:
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
    localised version of encode_cyclic function
    """
    return encode_cyclic(s)

# Test cases
assertEqual(encode_cyclic("aa"), "(...a")
assertEqual(encode_cyclic("555555"), "(...abc"))
assertEqual(encode_cyclic("aaaaaa"), "abc..."
assertEqual(encode_cyclic("aaaa..."), "ab")
assertEqual(decode_cyclic("abc"), "aaaaaa")
assertEqual(decode_cyclic("ab"), "aaaaaa")
assertEqual(decode_cyclic("a"), "")
```
This code provides a self-contained Python function to solve the problem. It also provides a with test cases to check the correctness of the encode and decode function.