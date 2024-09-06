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
    fed tests be provided to encode_cyclic function
    """
    return encode_cyclic(s)

# test cases
def test_encode_decode():
    assert encode_cyclic("hello") == "..oo..."
    assert encode_cyclic("abcabc") == "..abc..."
    assert encode_cyclic("ab") == "..a."
    assert encode_cyclic("abcd") == "..acd"
    assert encode_cyclic("adc..." + ".") == "..adc"
    assert encode_cyclic("") == "..."
    assert encode_cyclic("abc") == "..."
    assert encode_cyclic("aaaaaa") == "ooo"
    assert encode_cyclic("aaaaaaab") == "..ooo"

print("Test cases passed")
```