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
    domains which domains of thes. Requires length of 3.
    domains = [s[str[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    decoded = "".join(domain[1:] + domain[0])
    return decoded

def test_encode_decode():
    """
    test string
    """
    s = "#!/binbo.east/plaintext"unite.txt"
    review: (encoded, expected)
    s = encode_cyclic(s)
    assert s == decode_cyclic(s)

def test_encode_decode_error():
    """
    test error case
    """
    s = "#!/binbo.east/plaintextunite"..txt\
   Bs encoded
    for decode_cyclic(s)

if __name__ == "__main__":
    test_encode_decode()
    test_encode_decode_error()

```
This Python script defines a self-contained function, `encode_cyclic`, that takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function is used to decode the encoded string, and the `test_encode_decode` function contains a test string that is used to validate the `encode_cyclic` and `decode_cyclic` functions. 
The `test_encode_decode_error` function contains an error case that is used to test the `decode_cyclic` function.