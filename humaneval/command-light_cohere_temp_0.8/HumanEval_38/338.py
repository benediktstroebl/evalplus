```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    return ".join(groups)"

    # test
    assert encode_cyclic("hello") == "...hello"
    assert encode_cyclic("world") == "...world..."
    assert encode_cyclic("aaaa") == "...aaaa"
    assert encode_cyclic("ss") == "...css"
    assert encode_cyclic("xx") == "...xxx"
    assert encode_cyclic("aaa") == "aaaa"

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    agreed constraints.
    assert s == decode_cyclic("...aaaa")
    assert s == decode_cyclic("...")
    assert s == decode_cyclic("..aaaa")
    assert s == decode_cyclic("...")
    assert s == decode_cyclic("hellooo")
```
This script defines a function `encode_cyclic` that takes a string `s` as input and returns an encoded string by cycling groups of three characters. The string is split into groups of length 3, and each group is concatenated with the first character removed (to ensure all groups are of length 3). The `decode_cyclic` function takes the encoded string as input and returns the decoded string.