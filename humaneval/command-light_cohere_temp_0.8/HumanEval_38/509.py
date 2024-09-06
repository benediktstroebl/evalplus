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

    @ Allen4
    tests:
    """
    assert encode_cyclic("hello").rstrip() == "ohellolh"
    assert encode_cyclic("world").rstrip() == "dlrowo"
    assert encode_cyclic("hello world").rstrip() == "ohelldlrow"
    assert encode_cyclic("").rstrip() == ""
    assert encode_cyclic("python is great").rstrip() == "glgltre"
    assert encode_cyclic("  just words ").rstrip() == "jstwrog"
    assert encode_cyclic("hello123").rstrip() == "o123"
    assert encode_cyclic("\u4f53111").rstrip() == "\u4f"
    assert encode_cyclic("\u65e5\u6c34").rstrip() == "\ue"
    assert encode_cyclic("\u65E5\u6C34").rstrip() == "\ue"
    assert encode_cyclic("\n".join()).rstrip() == ""
    assert decode_cyclic("\u4f53111").rstrip() == "\u4f"
    assert decode_cyclic("\u65e5\u6c34").rstrip() == "\ue"
    assert decode_cyclic("\u65E5\u6C34").rstrip() == "hello"
    assert decode_cyclic("\n".join()).rstrip() == "\n"

This Python code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string `s` as input and returns the decoded string. 

The code also includes a series of tests to verify the functionality of the functions.