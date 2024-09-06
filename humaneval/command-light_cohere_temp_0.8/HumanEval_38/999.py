```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    partner for the 
    decode the string encoded by encode_cyclic.
    # The return the original string
    """
    return s

def test_encode_decode():
    """
    tests for encode_cyclic and decode_cyclic functions
    """
    s = "abcad"
    encoded = encode_cyclic(s)
    print("Encoded:", encoded)
    assert encoded == "d"
    print("Original:", s)
    decoded = decode_cyclic(encoded)
    print("Decoded:", decoded)
    assert decoded == s
    s = "fghijklmn"
    encoded = encode_cyclic(s)
    print("Encoded:", encoded)
    assert encoded == "klmn"
    decoded = decode_cyclic(encoded)
    print("Decoded:", decoded)
    s = "abcdefghijklmnopqr"
    encoded = encode_cyclic(s)
    print("Encoded:", encoded)
    assert encoded == "qr"
    decoded = decode_cyclic(encoded)
    print("Decoded:", decoded)

test_encode_decode()
```
The script defines two functions, `encode_cyclic` and `decode_cyclic`, which encode and decode markdown strings using a self-contained approach. The `test_encode_decode` function provides a set of tests to ensure the correctness of the `encode_cyclic` and `decode_cyclic` functions.