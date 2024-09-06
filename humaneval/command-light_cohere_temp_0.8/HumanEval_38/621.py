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
    both functions:
    1.
    -   Decodes the equal length 3 string to the original string.
    -   Tests the minimum character in each group.
    -   This other characters are appended to the beginning of each group.
    -   Returns the minimum length 3 string to the original string
    """
    return s.replace(lambda g: g.replace("".un-_", g[1:], "".join(groups)))

# run tests
def test_encode_decode():
    print(encode_cyclic("Hello World"))
    print(decode_cyclic("Hxl_v"))
    print(encode_cyclic("ABC"))
    print(decode_cyclic("A"))
    print(encode_cyclic("ABC"))
    print(decode_cyclic("AB"))
    print(encode_cyclic("-")))
    print(decode_cyclic("-"))
    print(encode_cyclic("A" + "B" + "C"))
    print(decode_cyclic("ACB"))
    print(encode_cyclic("12345"))
    print(decode_cyclic("12345"))

test_encode_decode()
```

The code defines a function `encode_cyclic` which returns the encoded string by cycling groups of three characters. The `decode_cyclic` function decodes the encoded string. The code also includes a function `test_encode_decode` to run the test cases for the `encode_cyclic` and `decode_cyclic` functions.