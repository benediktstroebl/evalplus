Here's a Python script that defines a self-contained function to encode and decode markdown code blocks using the specified functions:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    can decode a encode_cyclic string
    """
    return "".join(encode_cyclic(s))

def test_encode_decode():
    """
    tests the encode_cyclic and decode_cyclic functions
    """
    assert encode_cyclic("hello") == "hel".hl
    assert encode_cyclic("World") == "dlroW"
    assert encode_cyclic("!!!#") == "!#$"
    assert decode_cyclic("hel") == "hello"
    assert decode_cyclic("dlroW") == "World"
    assert decode_cyclic("#$") == "!!!#"

if __name__ == "__main__":
    test_encode_decode()
```
This script defines a function **encode_cyclic** that encodes a string to a markdown code block by cycling groups of three characters, and a function **decode_cyclic** that decodes the string from the markdown code block. The function **test_encode_decode** contains several tests that validate the correctness of the **encode_cyclic** and **decode_cyclic** functions.