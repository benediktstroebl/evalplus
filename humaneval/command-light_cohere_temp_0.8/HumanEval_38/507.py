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
    takes as input encoded string returned by encode_cyclic function. Returns decoded string
   
"""
    return s.encode_cyclic(s)

# test cases
def test_encode_cyclic():
    assert encode_cyclic("hello world") == "hello world"

def test_decode_cyclic():
    assert decode_cyclic("hello world") == "hello world"
```
This code contains two functions: encode_cyclic and decode_cyclic. The encode_cyclic function splits the input string into groups of three characters and cycles the characters within each group. The decode_cyclic function takes the encoded string as input and returns the decoded string. The code also contains test cases for both functions to verify their correctness.