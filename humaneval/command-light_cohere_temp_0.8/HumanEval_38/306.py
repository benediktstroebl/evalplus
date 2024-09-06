```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[::-1] for g in s[::3])

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
 """
    Test case 1:
    """
    assert encode_cyclic("") == ""
    assert encode_cyclic("abc") == "zab"
    assert encode_cyclic("xyz") == "yzx"

    """

    Test case 2:
    """
    # Encode same string twice.
    s = "abc"
    assert encode_cyclic(s) == encode_cyclic(s)
    assert encode_cyclic(s) == "zabzab"

    """

    Test case 3:
    """
    # Test empty string
    assert encode_cyclic("") == ""

    Test case 4:
    """
    # Test string with only one character
    assert encode_cyclic("a") == "a"

    """

    Test case 5:
    """
    # Test mixed strings
    assert encode_cyclic("abcde") == "czdez"
    assert encode_cyclic("xyzabc") == "yzxaz"
    assert encode_cyclic("abcdxzyx") == "zabcdxyzx"
```

The function `encode_cyclic` encodes a string to a new string with each three characters of the original string repeated to form a group, then reverses the characters in each group to "cycle" the groups. The function `decode_cyclic` then decodes the input string by reversing the characters in each group.