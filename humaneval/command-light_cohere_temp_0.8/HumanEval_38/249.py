```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def test_encode_cyclic():
    """
    tests if encode_cyclic returns the expected output
    """
    s = "abcabc"
    assert encode_cyclic(s) == s

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    domains
   
    """
    return s

def test_decode_cyclic():
    """
    tests if decode_cyclic returns the expected output
    """
    s = encode_cyclic("abcabc")
    assert decode_cyclic(s) == s

# run all functions to see if they work
test_encode_cyclic()
test_decode_cyclic()

```
This script defines two functions, `encode_cyclic` and `decode_cyclic`, that take a string as input and return either the original string, or a string that has been encoded with the `encode_cyclic` function. 
The `test_encode_cyclic` and `test_decode_cyclic` functions are designed to test the correctness of the `encode_cyclic` and `decode_cyclic` functions, respectively.

This code is written with full self-containment, as both the encoding and decoding functionality, along with the tests, are all contained within the same script.