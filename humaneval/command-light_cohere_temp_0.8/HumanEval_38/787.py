```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    common-case encoding and decoding for cyclic groups of characters.
    # encode string with cyclic groups of characters.
    return encode_cyclic(s)


# tests
test_encode_cyclic("hello")
# "hello" should be encoded correctly
test_encode_cyclic("world")
# "world" should be encoded correctly
test_encode_cyclic("!@#)
# should be encoded correctly
test_encode_cyclic("abc")
# should be encoded correctly
test_encode_cyclic("".join)
# empty string should be encoded correctly
test_encode_cyclic("abcde")
# any other string should be correctly encoded
test_decode_cyclic("hello")
# "hello" should be decoded correctly
test_decode_cyclic("world")
# "world" should be decoded correctly
test_decode_cyclic("abc")
# any other string should be decoded correctly
```