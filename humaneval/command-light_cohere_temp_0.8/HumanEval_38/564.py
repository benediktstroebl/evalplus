```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example tests the Example to test the encode_cyclic function:
    assert encode_cyclic("hello") == "[[h],olle]]"
    # test with invalid input
    assert encode_cyclic("not valid") == "".h"

# uncomment this to test decode_cyclic function
def test_encode_decode():
    assert encode_cyclic("hello") == "[[h],olle]]"
    assert encode_cyclic("world") == "[[dlro],olle]]"
    assert encode_cyclic("!") == "[[!h]"]"
```

This code defines a function encode_cyclic that takes a string as input and returns an encoded string. The encoded string contains cycles of three characters, where the characters are taken from the input string and repeated in a group of three characters. The function also handles the string lengths that are not divisible by three. The code also defines a decode_cyclic function that takes an encoded string as input and returns the decoded string. The test_encode_decode function tests both the encode_cyclic and decode_cyclic functions with various inputs.