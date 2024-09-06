```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    If groups of three characters exist, returns the original string.
    Otherwise, encode the string by cycling groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    if len(groups) == 1: return s
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    If guaranteed to be decoded correctly.
    """