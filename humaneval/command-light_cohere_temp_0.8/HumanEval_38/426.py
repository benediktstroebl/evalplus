```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    real case.

s = "aaaa"
encoded = encode_cyclic(s)
decoded = decode_cyclic(encoded)
assert encoded == decoded
```

This script defines a self-contained function called encode_cyclic, which performs the encoding and decoding process. The encode_cyclic function takes a string s as input and returns the encoded string. It works by splitting the string into groups of length 3 and then encoding each group by cycling its characters. The decoded string is then obtained by applying the decode_cyclic function to the encoded string.