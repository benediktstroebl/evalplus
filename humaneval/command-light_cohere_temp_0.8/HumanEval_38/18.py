```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    common input test string that has been encoded with encode_cyclic function.
    """
    test if input string is the decoded version of the string that was encoded using encode_cyclic function. 
    """
    test_if input is not the decoded version of the string, then the function will fail.
    """
    test that it is decoded successfully using decode_cyclic function.
    """
    test that the input is the same string that was used to encode it using encode_cyclic function.
    """
    test that the string is not valid.