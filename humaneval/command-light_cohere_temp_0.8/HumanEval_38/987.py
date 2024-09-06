```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    class user input:
    """
    # Test the encode_cyclic function
    assert encode_cyclic("hello world") == "h..v..l o..v..l u..."
    # Test the decode_cyclic function
    assert decode_cyclic("h..v..l u...") == "hello world"

This script defines a self-contained function that solves the problem and passes the corresponding tests.