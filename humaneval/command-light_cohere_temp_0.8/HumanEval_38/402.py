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
    time- string is correctly decoded.
    # The string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3
    # cycle elements in each group. If group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups
    return s.decode(groups)

# test
print(encode_cyclic("hello"))
print(decode_cyclic("hello")))
```

This script defines a self-contained function `encode_cyclic` that encodes a string to contain groups of three characters and a `decode_cyclic` function that decodes this string. The test section prints the both encoded and decoded strings for the input "hello".