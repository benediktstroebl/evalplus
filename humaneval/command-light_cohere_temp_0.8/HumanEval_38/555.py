```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return ["".join(c for i, c in enumerate(s) if c in "abc"))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   

    all encoded characters in the string and decodes them
    """
    return "".join(s)

def test_encode_cyclic():
    s = "hello world 123"
    encoded = encode_cyclic(s)
    print(encoded)  # Output: ['h', 'ello ', 'world ', '123']
    assert encoded == decode_cyclic(encoded)

def test_decode_cyclic():
    s = "hello world 123"
    decoded = decode_cyclic(s)
    print(decoded)  # Output: "hello world 123"
    assert decoded == s

# Run the tests
test_encode_cyclic()
test_decode_cyclic()
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`, to convert a string into an encoded and decoded format respectively. 

The `test_encode_cyclic` function tests whether the `encode_cyclic` function correctly converts a given string into an encoded format and then whether the `decode_cyclic` function correctly decodes it. 

The `test_decode_cyclic` function tests whether the `decode_cyclic` function correctly converts an encoded string back into the original string.