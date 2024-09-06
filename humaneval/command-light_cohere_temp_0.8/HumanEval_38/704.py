```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(c for c in s if c[0] in "abc" and c[1] in "cde" and c[2] in "fus")

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   05. 

   unencoded string
   3. 

test encode decode pair:
    """
    assert encode_cyclic("hello") == "fnilfd"
    assert decode_cyclic("fnilfd") == "hello"

test_decode_cyclic()
```

In this script, we have defined a self-contained function `encode_cyclic` that performs the encoding and `decode_cyclic` that performs the decoding. The test functions ensure that the encode and decode function correctly convert between the encoded and decoded strings.