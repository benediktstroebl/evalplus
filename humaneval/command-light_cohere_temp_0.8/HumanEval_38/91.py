Here is a Python script that encodes and decodes markdown code blocks using a self-contained function:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group, and leave off the first character and the last character
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    brother problem"""
    return s.