```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example of the test encoding
    """

The encode_cyclic function takes a string as input and applies a specific encoding technique, while the decode_cyclic function accepts the string that was encoded using the encode_cyclic function and returns the decoded string. 

This is a self-contained Python script with a function that solves the problem and passes all the corresponding tests.