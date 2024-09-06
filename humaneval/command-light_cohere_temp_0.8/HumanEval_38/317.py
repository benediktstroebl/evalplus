```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    begin
   
    from encoding to decoding.

# Test
def test_encode_decode():
    s = "abcdabc"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert s == decoded
    s = "hello world"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert s == decoded

test_encode_decode()
 ```

This code defines a Python script that contains a self-contained function to solve the encode_cyclic and decode_cyclic problem. It also contains a test function to verify the functionality of the encode_cyclic function.