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
    the expect
    base64" decryption
    """
    return s.decode(groups)

# encode and decode test
s = "abcabc123"
encoded = encode_cyclic(s)
decoded = decode_cyclic(encoded)
print(f" Original: {s}, Encoded: {encoded}, Decoded: {decoded}")
```

This script provides a function to encode a string with a specific pattern and another function to decode the string.

The `encode_cyclic` function takes a string as input and splits it into groups of three characters. It then cycles through each group of three characters, and returns the decoded string. The `decode_cyclic` function takes the encoded string as input and returns the decoded string, which is the original string without the cyclic pattern.

The script also includes two test cases, and it prints the original string, the encoded string, and the decoded string for each test case.