```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return s[:(3 * len(s) // 3)] + s[(len(s) - 3 * len(s) // 3: len(s)]

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
   """
This is a self-contained Python script that defines two functions: `encode_cyclic` and `decode_cyclic`, that solve the given problem. The `encode_cyclic` function returns the encoded string by cycling groups of three characters, and the `decode_cyclic` function takes an encoded string as input and returns the decoded string.