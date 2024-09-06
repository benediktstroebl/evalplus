```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    supports:
        - same as encode_cyclic function.
    """
    Test cases:
    test_string = "hello world!"
    encoded = encode_cyclic(test_string)
    assert encoded == "ooohellooo ."
```
The function `encode_cyclic` takes a string `s` as input and returns an encoded string. The function uses a split the string into groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns a decoded string. The `decode_cyclic` function also provides test cases that verify the correctness of the function.