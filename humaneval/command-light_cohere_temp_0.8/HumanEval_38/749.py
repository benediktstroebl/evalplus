```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    simplest test that string cycle.
    decoded = s[:(len(s) + 2) // 3]
    return decoded

def test_encode_decode():
    """
    test the encode_decode function
    """
    s = "ahmed test Encoded test"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    print("test encoded:", encoded)
    print("test decoded:", decoded)
    assert encoded == decoded

test_encode_decode()
```
This code defines two functions: **encode_cyclic** and **decode_cyclic**. The first one splits a string into groups of three characters and cycles the characters within each group. The second one simply decodes the string by removing the cycle applied in the first function.