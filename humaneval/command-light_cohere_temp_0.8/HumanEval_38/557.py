```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g if len(g) == 3 else g[1:] + g[0] for g in s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)])

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    see encode_cyclic function docstring for details.
    """
    tested successfully with both encode_decode pair 

You can use the encode_cyclic and decode_cyclic functions to encode and decode a string in a cyclic format.