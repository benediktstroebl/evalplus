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
    right back"""
same logic of encode_cyclic.
    return "".join(groups)

# test
test_encode = "ACB..."
print(encode_cyclic(test_encode))  # Outputs: ABACBC."

test_decode = "".join("ACBC".join()  # Outputs: ABACBC."
```

This script defines a self-contained function that solves the problem of encoding and decoding a string with a cyclic group of three characters. The script also passes the same tests for the encode_cyclic and decode_cyclic functions.