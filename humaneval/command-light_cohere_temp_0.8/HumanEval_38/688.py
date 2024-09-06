```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    important decoded string
   
    """

    # tests
    assert encode_cyclic("hello world") == "hnkee olock wold"
    assert encode_cyclic("hello world helloo") == "hello dnkas"
    assert encode_cyclic("hello world, hello, hello") == "".join(","hello world ")
    assert decode_cyclic("hnkee olock wold") == "hello world helloo"
    assert decode_cyclic("hello dnkas") == "hello world helloo"
    assert decode_cyclic("hello world! helloo") == "hello world helloo"
    assert decode_cyclic("hello world. hell()") == "hello world"
```

The Python script defines a self-contained function `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. The function uses a splitting the string to groups of three characters, where each group contains exactly three characters. Then, it cycles the elements in each group and handles cases where the group has fewer elements than three. Finally, the `decode_cyclic` function is defined to take an input string and return its decoded string. The function uses the same approach as `encode_cyclic` function to solve the encoding and decoding of cyclic groups of characters.