```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
"""
    # Test
    assert encode_cyclic("...") == ".---..."
    assert encode_cyclic(".") == ".--."
    assert encode_cyclic("aa") == "---aa"
    assert encode_cyclic(" Flavors are great!") == "Flavors--reat-ge---"
    assert encode_cyclic(" Concius est un animal francais") == "Con--ci-s--ut-un--r--anim--franc--"
    # Actual decoding
    assert decode_cyclic("...") == "."---."
    assert decode_cyclic("---") == "Flavors are great!"
    assert decode_cyclic("---") == "Con--ci-s--ut-un--r--anim--franc--"
```
The provided Python script defines a self-contained function `encode_cyclic` that takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an input string and returns its decoded version.