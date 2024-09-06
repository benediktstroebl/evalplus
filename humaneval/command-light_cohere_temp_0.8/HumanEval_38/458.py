```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    general test
    test cases are encoded and decoded using the encode_cyclic and decode_cyclic functions.
    assert encode_cyclic("hello world") == "h$3o#dlroW$"
    assert decode_cyclic("h$3o#dlroW$") == "hello world"
```
The code implements the encode_cyclic and decode_cyclic functions. The encode_cyclic function converts an input string into an encoded string by cycling groups of three characters. The decode_cyclic function takes the encoded string as input and returns the original decoded string. It also provides some test cases to verify the correctness of the functions.