```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    Develop an the approach:
        1. Input a string that must be a string that can be encoded by the encode_cyclic function.
        2. It must return theupa string that can be decoded by the decode_cyclic function.
    """
    test_encode_cyclic(u": "hello world!> encode_cyclic))
    assert s == "h@##$dlrung#"
    test_decode_cyclic("h@##$dlrung#")
    test_decode_cyclic(" heading there")
    test_decode_cyclic("hello world")
    test_decode_cyclic(" It's all about you ")
```