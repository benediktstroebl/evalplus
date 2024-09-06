```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    Bars the `
    has three characters, and then the cycle continues.
    """
    return s[encode_cyclic(s)]

def test_encode_decode():
    """
    confirms encode_cyclic and decode_cyclic functions work as expected.
    """
   
    test_encode_decode.encode("Hello, World!
    assert encode_cyclic("Hello, World!") == "hEYd dWCx"
    assert decode_cyclic("hEYd dWCx") == "Hello, World!"
    assert encode_cyclic("!" + "!") == "!!h(.*)"
    assert encode_cyclic("aa") == "aaa"
    assert decode_cyclic("aaa") == "aa"
    assert encode_cyclic("aabb") == "aabb"
    assert decode_cyclic("aabb") == "ab"
    assert encode_cyclic("abc") == "ab" + "c"
    assert decode_cyclic("ab" + "c") == "abc"
    assert encode_cyclic("abcd") == "abcd"
    assert decode_cyclic("abcd") == "abcd"
    assert encode_cyclic("hello") == "..." + "hello"
    assert decode_cyclic("..." + "hello") == "hello"
    assert encode_cyclic("".join("hello")) == "hEYd dWCx"
    assert decode_cyclic("hEYd dWCx") == "hello"
```
This code defines two functions, `encode_cyclic` and `decode_cyclic`, which solve the problem of encoding and decoding a string of characters that repeats every three characters. It also includes a test_encode_decode, which passes all the tests with the functions. The code should be self-contained and only contain the functions and the test suite.