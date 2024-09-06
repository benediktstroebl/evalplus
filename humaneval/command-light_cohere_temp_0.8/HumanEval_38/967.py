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
    need to test the string encoded with encode_cyclic function
    """
    return encode_cyclic(s) == s

def test_encode_decode():
    """
    test cases
    """
    assert encode_cyclic("Hello") == "H" + "llod"
    assert encode_cyclic("World") == "W" + "rld"
    assert encode_cyclic("!!!oz") == "..." + "oz"
    assert encode_cyclic("") == ""
    assert encode_cyclic("Python is great!") == "Py" + "t" + "ni" + "gs"
    assert decode_cyclic("H") == "hello"
    assert decode_cyclic("W") == "world"
    assert decode_cyclic("oz") == "oz"
    assert decode_cyclic("") == ""
    assert decode_cyclic("Python") != "Python" + "is"
    assert decode_cyclic("great") == "great"

if __name__ == "__main__":
    test_encode_decode()
```
The code you provided defines a Python script with a self-contained function that solves the problem of encoding and decoding strings with circular groups of three characters. It also has several test cases to verify the correctness of the encode_cyclic and decode_cyclic functions.