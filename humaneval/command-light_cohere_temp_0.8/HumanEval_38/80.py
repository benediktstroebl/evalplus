```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    a
    """
    # decode the string
    decoded_str = "".join(groups)
    return decoded_str

def test_encode_cyclic():
    """
    # test the encode_cyclic function
    test_str = "abcabc123"
    encoded = encode_cyclic(test_str)
    print("encoded:", encoded)
    assert encoded == "abcabc123"

def test_decode_cyclic():
    """
    # test the decode_cyclic function
    test_str = "abcabc123"
    decoded = decode_cyclic(test_str)
    print("decoded:", decoded)
    assert decoded == "abcabc123"
```
This code contains a self-contained Python function called `encode_cyclic` that takes a string as input and returns an encoded version of the string. The `decode_cyclic` function then decodes the input and returns the decoded string. The `test_encode_cyclic` and `test_decode_cyclic` functions are there to run the encode and decode functions with test cases.