```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    observed behavior matches the important requirements.
    """
    expected behavior is an input string with groups of three characters,
    "abc", "abcabc", "abcabcabc", etc. The output string should be "abcabcabc".
"""
def test_encode_decode():
    assert encode_cyclic("abc") == "abcabcabc"
    assert encode_cyclic("ab") == "abcab"
    assert encode_cyclic("abc") == "abcabcabc"
    assert encode_cyclic("abcd") == "cdabcd"
    assert encode_cyclic("cbb") == "cbbcb"
    assert encode_cyclic("b") == "bab"
    assert encode_cyclic("babc") == "bababc"
    assert encode_cyclic("abcbb") == "abcbbcb"
    assert encode_cyclic("bbbc") == "bcabbc"
    assert encode_cyclic("b") == "bab"
    assert encode_cyclic("") == ""
    assert encode_cyclic("x") == ""
    assert encode_cyclic("\n") == ""

if __name__ == "__main__":
    test_encode_decode()
```
This Python script defines a function called `encode_cyclic` that takes a string as input and returns a new string with groups of three characters. The function splits the strings into groups of three characters using the given string's characters as the first and last characters in each group. The resulting string is then those groups in a cyclical manner. 

The `decode_cyclic` function is defined to take an input string that was encoded using the `encode_cyclic` function. It returns the strings in a linear manner. The `test_encode_decode` function contains a series of assert statements that test the `encode_cyclic` and `decode_cyclic` functions with various input strings.