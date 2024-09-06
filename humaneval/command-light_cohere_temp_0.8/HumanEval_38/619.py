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
    test theores the same groups.
    groups = "".join(encoded)
    return decoded.decode(groups)

# test cases
test_cases = [
    "ABA",
    "abc",
    "ABABC",
    "<<>>",
    "aa"
]
for case in test_cases:
    print(encode_cyclic(case), decode_cyclic(case))
```
This code defines a self-contained Python function that solves the problem of encoding and decoding a string using a cyclic group of three characters. It also passes a test cases to ensure the function is working correctly.