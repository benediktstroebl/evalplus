```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(encode_cyclic_helper(groups) for groups in s.array(group, 3, 0))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
"""
    return "".join(decode_cyclic_helper(groups) for groups in s.array(group, 3, 0))

def encode_cyclic_helper(groups):
    """
    creates list of array of length 3 from each group of 3 characters, and adds them to the list
    """
    return [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]

def decode_cyclic_helper(groups):
    """
    returns list of decoded strings, from the input list of length 3 arrays
    """
    return [groups[i] for i in range(len(groups))]

# test cases
def test_encode_cyclic():
    assert encode_cyclic("Hello World") == "H@dlod Ollehh4"

def test_decode_cyclic():
    assert decode_cyclic("H@dlod Olleh4") == "Hello World"

```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, that solve the given problem. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns a decoded string. The script cases test the correctness of the functions.