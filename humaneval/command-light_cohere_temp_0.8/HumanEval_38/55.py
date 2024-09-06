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

    @tests:
    assert encode_cyclic("hello") == "hhellod"
    assert encode_cyclic("world") == "dlroww"
    assert encode_cyclic("!") == "!!!h"
    assert decode_cyclic("hhellod") == "hello"
    assert decode_cyclic("dlroww") == "world"
    assert decode_cyclic("!") == "!"
```
This Python script defines a self-contained function, `encode_cyclic`, which takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an input string and returns the decoded string. The function is tested by asserting that its output matches the expected result for a variety of input strings.