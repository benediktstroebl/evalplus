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
    goal is input is the encoded string from encode_cyclic function.
    return s
 goal is to pass the tests and have the decoded string decoded_string be the same.

tests = [
    ("hello", "hello"),
    ("<html", "<html"),
    # not a three-letter group
    ("abc", "def"),
    # empty string
    ("", "")
]

for input, expected in tests:
    actual = encode_cyclic(input)
    assert actual == expected
```