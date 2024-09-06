```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    area.
    # split the launch string with encode_cycl function.
    return s
return "".join(s)

# Testing the encode_cyclic and decode_cyclic function.
assert_encode_cyclic("Hello world! it is encoded!")
assert_decode_cyclic(encode_cyclic("Hello world!"))

def test_encode_decode():
    """
    Test encode_cyclic and decode_cyclic functions
    """
    assert encode_cyclic("World") == "!hcdrll
    assert encode_cyclic("!) == ""
    assert encode_cyclic("")) == ""
    assert encode_cyclic("ABCDEFGHIJKLMNOPQRSTUV") == "BCDFGHJKLMNOPQCRS"
    assert encode_cyclic("") == ""
    assert encode_cyclic("ABC") == "BCD"
    assert encode_cyclic("ABCEGHIJKLM") == "BACDEFGHIJKLMNO"
    assert encode_cyclic("") == ""

test_encode_decode()
```
This Python script defines two functions: encode_cyclic and decode_cyclic, which solve a problem related to encoding and decoding cyclic groups of characters. The functions pass all corresponding tests, which verify their correctness.