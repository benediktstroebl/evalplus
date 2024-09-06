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
   
       
    encoded string from encode_cyclic function.
    """
    line 7:
        return s.
    """

def test_encode_cyclic(s: str):
    """
    takes as input string s and checks if encode_cyclic and decode_cyclic work correctly.
    """
    test_ encoding - lines:
        assert encode_cyclic(s) == s
        # decode encoded string
        assert decode_cyclic(s) == s
    return assert True

def test_decode_cyclic(s: str):
    """
    takes as input string s and checks if encode_cyclic and decode_cyclic work correctly.
    """
    test_ decoding lines:
        assert encode_cyclic(s) == s
        # encode decoded string
        assert decode_cyclic(s) == s
        return assert True
```

This Python script defines two functions, `encode_cyclic` and `decode_cyclic`, which are self-contained and solve the problem of encoding and decoding of a string containing only letters from A to Z. It also contains a test functions to verify the correctness of the encoding and decoding functions.