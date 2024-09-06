```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    support testing the
 test the encode_cyclic and decode_cyclic functions.
    assert encode_cyclic("hello") == "cycleseicleh"
    assert encode_cyclic("world") == "cyclowrd"
    assert encode_cyclic("map") == "aciplmap"
    assert encode_cyclic("") == ""
    assert decode_cyclic("cycleseicleh") == "hello"
    assert decode_cyclic("cyclowrd") == "world"
    assert decode_cyclic("aciplmap") == "map"
    assert decode_cyclic("") == ""
```
This Python script defines two functions, `encode_cyclic` and `decode_cyclic`, which are used to convert and decode a string containing Markdown code into a plain string, respectively. The `assert` statements are used to test the functions and verify their correctness.