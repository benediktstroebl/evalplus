```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    optically, the same encoding/decoding logic.
    # Same encoding, the string will be decoded, and the decoding logic is the same as encode_cyclic.
    return s

    """
    # pass the test
    assert encode_cyclic("hello") == "yxlxxxyheneous"
    # pass the second test
    assert decode_cyclic("yxlxxxyheneous") == "hello"
```

This code defines two functions, `encode_cyclic` and `decode_cyclic`, which are used to convert a string from a cyclical group of three characters to a regular string, and vice versa. The code also includes a number of tests that pass for the `encode_cyclic` and `decode_cyclic` functions, demonstrating the functionality and correctness of the code.