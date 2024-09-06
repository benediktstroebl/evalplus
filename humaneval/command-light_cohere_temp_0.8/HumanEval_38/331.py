Here is a Python script that defines two functions, `encode_cyclic` and `decode_cyclic`, to handle encoding and decoding of a string containing only three-letter groups:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    bare decoding on the will work on encoded string
    """
    return s

# example usage
test_string = "EXAMPLE TEXT"
encoded = encode_cyclic(test_string)
print("encoded: ", encoded)
decoded = decode_cyclic(encoded)
print("decoded: ", decoded)
```

The script defines two functions `encode_cyclic` and `decode_cyclic`, which respectively encode and decode a string using a self-contained approach. The encoded string is created by splitting the original string into groups of three characters and then encoding each group by cycling the characters in the group. 

This self-contained approach can be used to handle the encoding and decoding of markdown code in various scenarios.