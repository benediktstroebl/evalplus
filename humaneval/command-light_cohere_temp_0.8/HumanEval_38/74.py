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
    right input encoded string.
    Returns the right only string to match that of the encode_cyclic function.
    return decode_cyclic(s)

def test_encode_decode():
    s = "abcabcab"
    assert encode_cyclic(s) == "acd"
    s = "......."
    assert encode_cyclic(s) == "......."
    s = "..."
    assert encode_cyclic(s) == ""
    s = "a" * 1000
    assert encode_cyclic(s) == ""

# this code
test_encode_decode()
 ``` 
This Python code defines a self-contained function that performs the problem of encoding and decoding strings with cycles of three characters. The encode_cyclic function splits the input string into groups of three characters and cycles the elements within each group. The function then returns the string that was encoded. The decode_cyclic function takes the input string and returns the decoded version of the string. The test_encode_decode function is used to verify the correctness of the encode_cyclic and decode_cyclic functions by testing with different input strings.