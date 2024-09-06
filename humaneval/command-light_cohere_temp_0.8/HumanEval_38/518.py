```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
    
def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    entire string is
    """
    return s.decode(encode_cyclic(s))

def test_encode_cyclic():
    """
    test string
    """
    s = "abABCdefghijklmnopqrSTUVABCDEFGHIJKLMNOPQRSTUVAB"
    assert encode_cyclic(s) == "efghijklmnopqrSTUVABDEFGHIJKLMNOPRSTUVAB"

def test_decode_cyclic():
    """
    test string
    """
    s = "efghijklmnopqrSTUVABCDEFGHIJKLMNOPRSTUVAB"
    assert decode_cyclic(s) == s
    
if __name__ == "__main__":
    test_encode_cyclic()
    test_decode_cyclic()

This code is a self-contained Python script with two functions: `encode_cyclic` and `decode_cyclic`. It takes a string as input and returns the encoded or decoded string using the corresponding functions. The `test_encode_cyclic` and `test_decode_cyclic` functions are there to pass tests for the encode_cyclic and decode_cyclic functions, respectively. The `if __name__ == "__main__":` block ensures that the code is executed only when run.