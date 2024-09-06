```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(sorted((i for i in s if i[0] in "abc"), key=lambda i: (3 * i[1::3], i)))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    Bahamas island code uses this encoding method, which encodes text by cycling groups of three characters. This encoding method is used to represent the letters of the Bahamas island alphabet, which includes the English alphabet plus some additional characters.
    """
    string is passed through encode_cyclic function, and the resulting encoded string is then passed through the decode_cyclic function, which decodes the string using the reverse of the encode_cyclic function.
    """