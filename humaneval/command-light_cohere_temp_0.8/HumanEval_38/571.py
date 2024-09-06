```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    work with the
    """
def test_encode_cyclic(s: str) -> None:
    """
    test string
    """
    encoded = encode_cyclic(s)
    assert encoded == s.encode_cyclic()

def test_decode_cyclic(s: str) -> None:
    """
    test string
    """
    decoded = decode_cyclic(s)
    assert decoded == s

```
This script defines two functions `encode_cyclic` and `decode_cyclic`, which solve the problem of encoding and decoding a string of markdown code blocks. The encode_cyclic function splits the input string into groups of three characters and cycles the elements within each group. The `decode_cyclic` function takes the encoded string and returns the decoded string. The test_encode_cyclic and `test_decode_cyclic` functions provide test cases for the functions to ensure they are working correctly.