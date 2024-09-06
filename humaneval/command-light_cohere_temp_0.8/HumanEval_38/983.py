```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    open-source string in HTML format
    """
    return "".join(s)

def test_encode_decode():
    """
    test case for encode and decode
    """
    input_str = "abcabc123"
    encoded = encode_cyclic(input_str)
    decoded = decode_cyclic(encoded)
    print("Input String:", input_str)
    print("Encoded String:", encoded)
    print("Decoded String:", decoded)

test_encode_decode()
```

The above code defines the functions `encode_cyclic` and `decode_cyclic`, which encode and decode a string containing only the characters 'a', 'b', and 'c'. The `test_encode_decode` function has a simple test case for the `encode_cyclic` and `decode_cyclic` functions.