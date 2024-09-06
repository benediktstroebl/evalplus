```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    accepts as an encoded string that was created with encode_cyclic function.
    """
    test encode_cyclic('a')
    should return 'ACTUCC'

# Test two
test_encode_cyclic('hello')
test_encode_cyclic('world')

test_decode_cyclic('ACTUCC')
test_decode_cyclic('hello')
test_decode_cyclic('world')
```
This script defines a function called **encode_cyclic** which takes a string s and returns an encoded string by cycling groups of three characters. The function also defines a function called **decode_cyclic** which takes an encoded string s and returns the decoded string.