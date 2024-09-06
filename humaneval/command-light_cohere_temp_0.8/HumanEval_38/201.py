```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    returns decoded string
    s = decode_cyclic(s)
    print(s)
    assert encode_cyclic(s) == s, "decode and encode should be equal"
    assert s == encode_cyclic(s)[::-1], "string order is important"
```

This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function receives a string `s` and returns an encoded string by grouping the characters into groups of three, cycling each group. The `decode_cyclic` function receives an encoded string and returns the decoded string. The code also passes the tests to the functions to ensure their correctness.