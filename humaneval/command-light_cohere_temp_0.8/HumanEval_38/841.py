Here's a Python script with a self-contained function that solves the problem of encoding and decoding strings containing only the characters a, b, and c, using a cyclic group of three characters:
```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    same
   ` cycle encoded string and returns decoded string
    """
    return s.encode_cyclic()

# Example test cases
def test_encode_decode():
    assert encode_cyclic("abcc") == "acb"
    assert encode_cyclic("acdb") == "abcd"
    assert encode_cyclic("bc") == "d"
    assert encode_cyclic("d") == "abcd"
    assert encode_cyclic("bcde") == "d"
    assert encode_cyclic("efg") == "efg"

def test_decode_cyclic():
    assert decode_cyclic("acb") == "ab"
    assert decode_cyclic("abcd") == "abc"
    assert decode_cyclic("d") == "abcd"
    assert decode_cyclic("efg") == "efg"

test_encode_decode()
test_decode_cyclic()

```
This Python script defines two functions, `encode_cyclic` and `decode_cyclic`, that handle the encoding and decoding of strings using a cyclic group of three characters. The `test_encode_decode` and `test_decode_cyclic` functions are provided to run self-contained tests on the encoding and decoding functions.