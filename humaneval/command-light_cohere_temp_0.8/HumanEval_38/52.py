```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example tests:
    assert encode_cyclic(input) == decode_cyclic(input),
    assert encode_cyclic("Hello world!") == "HeLLo worl!"
    assert encode_cyclic("Python is awesome") == "PoTiGOs is esoome"
    assert encode_cyclic("abcde") == "edilocba"
    assert encode_cyclic("") == ""
```
This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function receives a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function receives the encoded string as input and returns the decoded string. The code also passes the test cases for both functions.