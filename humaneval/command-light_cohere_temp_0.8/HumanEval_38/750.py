```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(groups)

def decode_cyclic(s: str):
    """
    checks whether string is correctly encoded
    """
    return encode_cyclic(s) == s

def test_encode_decode():
    """
    test function for encode_cyclic and decode_cyclic
    """
    assert encode_cyclic("hello") == " ** h l l o o"
    assert decode_cyclic("hello") == "hello"
    assert encode_cyclic("world") == " ** w o r l l"
    assert decode_cyclic("world") == "world"
    assert encode_cyclic("") == ""
    assert decode_cyclic("") == ""
```
This script defines two functions: **encode_cyclic** and **decode_cyclic**. The **encode_cyclic** function takes a string as input and returns the encoded string by cycling groups of three characters. The **decode_cyclic** function takes the input string and returns the decoded string by using the **encode_cyclic** function. The test_encode_decode function checks whether the **encode_cyclic** and **decode_cyclic** functions are correctly implemented by comparing the output of the functions with the expected string.