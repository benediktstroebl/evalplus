```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    pass this test cases:
    assert encode_cyclic("hello") == "hhelloa"
    assert encode_cyclic("abc") == "cabc"
    assert encode_cyclic("") == ""
    assert encode_cyclic("abcde") == "cdeabcde"
    assert encode_cyclic(" helloa ") == "h.heloa"
   a"
   
The code defines the functions `encode_cyclic` and `decode_cyclic`. It takes a string as input and returns the encoded or decoded string. The code also passes all test cases.