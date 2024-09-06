```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   ..."
    return s

def test_encode_decode():
    """
    passes test cases for encode_cyclic and decode_cyclic functions
    """
    assert encode_cyclic("hello world") == "h.vo"
   ns llode_world== "hello world"
    assert encode_cyclic("abc") == "a.bcbc"
   ns llode_world== "abc"
    assert encode_cyclic("abcabc") == "a.abcc"
     llode_world== "abcabc"
    assert encode_cyclic("abcabcabc") == "aa.bccc"
   
       llode_world = "abcabcabc"
    assert decode_cyclic("h.ov") == "hello world"
    assert decode_cyclic("a.b") == "abc"
    assert decode_cyclic("aa.bbabc") == "abcabc"
    assert decode_cyclic("a.abc.c") == "abc"
```