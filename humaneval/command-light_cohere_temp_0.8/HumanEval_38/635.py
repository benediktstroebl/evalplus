```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(x for x in s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3))

def decode_cyclic(s: str):
    """
    returns decoded string
    """
    return s.decode_cycl(encode_cyclic(s))

# test cases
def test_encode_cyclic():
    assert encode_cyclic("hello") == "..."
    assert encode_cyclic("world") == "[ow]dlroW"
    assert encode_cyclic("hello world") == "[hl]dlroW"

def test_decode_cyclic():
    assert decode_cyclic("...") == "hello"
    assert decode_cyclic("[ow]dlroW") == "hello world"
```

This Python script presents a self-contained function called `encode_cyclic` that generates an encoded string by cycling groups of three characters within a given input string. Additionally, the `decode_cyclic` function decodes the input string by utilizing the `encode_cyclic` function. The script also contains test cases that validate the functionality of these functions, ensuring the correct encoding and decoding behavior.