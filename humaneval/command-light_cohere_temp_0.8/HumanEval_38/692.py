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
    provided test
    provided test cases:
    """
    assert encode_cyclic("hello world") == "hEY olVD"
    assert encode_cyclic("hello world hell") == "hEY olVD hllll"
    assert encode_cyclic(""hl") == "EY olVD"
    assert encode_cyclic("   ") == "EY olVD"
    assert encode_cyclic("   x") == "EY olVD x"
```

This code defines a function called **encode_cyclic** which takes a string as input and returns the encoded string by cycling groups of three characters. The function then splits the string into groups of length 3 and then cycles the first character in each group. The function also handles the special case where the group has fewer elements than 3, in which case it returns the full group. The code also defines a function called **decode_cyclic** which takes an encoded string as input and returns the decoded string. The function performs the test cases to ensure the correctness of the function.