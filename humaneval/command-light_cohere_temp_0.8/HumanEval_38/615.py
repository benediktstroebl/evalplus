```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [['' + c for c in s[i:min(i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group.
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    test: "abcABC" -> "abcabc"
    """
    return s.encode_cyclic()

def test_encode_cyclic():
    s = "abcABC"
    encoded = encode_cyclic(s)
    assert encoded == "abcabc"

def test_decode_cyclic():
    s = "abcABC"
    decoded = decode_cyclic(s)
    assert decoded == "abcABC"
```
The above script defines two functions: encode_cyclic and decode_cyclic. The encode_cyclic function splits the input string into groups of length 3 and cycles each group. The decode_cyclic function takes an encoded string and returns the decoded version of that string. The test_encode_cyclic and test_decode_cyclic functions test the correctness of their respective functions.