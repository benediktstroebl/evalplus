```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    purpose of this testing that the original string was encoded with encode_cyclic.
    """
    test(encoded, 'decoded'))
    """
    return decode_cyclic(encoded)

def test_encode_decode():
    """
    string = "hello world"
    encoded = encode_cyclic(string)
    assert encoded == "h.heloo"
   
    decoded = decode_cyclic(encoded)
    assert decoded == "hello world"

test_encode_decode()
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. 

The `test_encode_decode` function contains the purpose of testing the functionality of the `encode_cyclic` and `decode_cyclic` functions. 

This script can be used as a reference for testing and understanding the functionality of your code.