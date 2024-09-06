```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
Tries are tests to decode_cyclic function
    """
    assert encode_cyclic(s) == s, "decode and encode should be equal"
    assert encode_cyclic("") == decode_cyclic(""), "top-level encode and decode should work"
    assert encode_cyclic("abc").encode_cyclic() == "abc", "encode works"
    assert encode_cyclic("abcde").encode_cyclic() == "abcde", "encode works"

def test_encode_decode():
    s = "aabb"
    encode = encode_cyclic(s)
    decode = decode_cyclic(encode)
    assert decode == s, "decode does not work"

if __name__ == "__main__":
    test_encode_decode()
```

This code defines two functions: `encode_cyclic` and `decode_cyclic`. The first one takes a string as input and returns an encoded string by cycling groups of three characters. The second one takes the string as input and returns the decoded string. Both functions are then tested by passing the `test_encode_decode` function, which contains assertions to check if the functions are working as expected.