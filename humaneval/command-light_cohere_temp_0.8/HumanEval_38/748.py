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
   
    get string back to decode, decode_cyclic function.
    return "".join(decode(s))

def encode(s: str):
    """
    returns encoded string by cycling groups of two characters.
    groups = s[(i):min((i + 3), len(s))] for i in range(len(s) // 2)
    # cycle elements in each group. Unless group has fewer elements than 2.
    groups = [(group[1:] + group[0]) if len(group) == 2 else group for group in groups]
    return "".join(groups)

def decode(s: str):
    """
    takes as input string encoded with encode function. Returns decoded string.
    return "".join(decode(s))

def test_encode_cyclic():
    s = "abcabcbb"
    encoded = encode_cyclic(s)
    print(encoded)
    assert encoded == "abc..."

def test_decode_cyclic():
    s = "abcabcbb"
    decoded = decode_cyclic(s)
    print(decoded)
    assert decoded == "abcabcbb"

def test_encode():
    s = "abc"
    encoded = encode(s)
    print(encoded)
    assert encoded == "abc"

def test_decode():
    s = "abc"
    decoded = decode(s)
    print(decoded)
    assert decoded == "abc"
```

This script defines three functions:
- encode_cyclic: This function takes a string s as input and encodes it by cycling groups of three characters. The function splits the string into groups of length 3 and cycles the elements in each group. The function then joins the elements back into a string and returns the result.
- decode_cyclic: This function takes an encoded string s as input and decodes it by reversing the encode_cyclic function. The function then joins the elements back into a string and returns the result.
- encode: This function takes a string s as input and encodes it by cycling groups of two characters. The function splits the string into groups of length 2 and cycles the elements in each group. The function then joins the elements back into a string and returns the result.
- decode: This function takes an encoded string s as input and decodes it by reversing the encode function. The function then joins the elements back into a string and returns the result.

The script also includes two test functions:
- test_encode_cyclic: This function tests the encode_cyclic function by passing an input string and expected output. The function then prints the expected output and asserts that the actual output is equal to the expected output.
- test_decode_cyclic: This function tests the decode_cyclic function by passing an input string and expected output. The function then prints the expected output and asserts that the actual output is equal to the expected output