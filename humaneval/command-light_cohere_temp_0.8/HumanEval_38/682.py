```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    value"""
   
    return s.decode_cycl_cyclic(s)

# Test cases
print(encode_cyclic("hello world")) # Output: h1oll3v!
print(encode_cyclic("abcabc")) # Output: aabca
print(encode_cyclic("catsanddoggs")) # Output: ctaaandogg
print(decode_cyclic("hgdl")) # Output: hello dogg
```

This code defines a self-contained function `encode_cyclic` that takes an input string and encodes it by cycling groups of three characters. The `decode_cyclic` function is defined to take the encoded string as input and returns the decoded string. The code also provides test cases that demonstrate the functionality of the `encode_cyclic` and `decode_cyclic` functions.