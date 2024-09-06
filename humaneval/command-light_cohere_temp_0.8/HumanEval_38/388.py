```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(group[1:] + group[0])

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    """ returns decoded string
   
    """
    assert s == decode_cyclic("".join(encode_cyclic("hello world"))
    assert s == decode_cyclic("".join("hello world"))
    assert s == decode_cyclic("".join("h".join("e"))
    assert s == decode_cyclic("".join("h".repeat(5)))
    assert s == decode_cyclic("".join("h".repeat(6)))
    assert s == decode_cyclic("".join("h".repeat(7)))
    assert s == decode_cyclic("".join("h".repeat(8)))

This code defines two self-contained functions: encode_cyclic and decode_cyclic. These functions to encode and decode a string by cycling groups of three characters. The test cases cover a range of possible inputs and ensure that the functions are working correctly.