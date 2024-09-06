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
    judge by decoded string and encoded string.
    assert encode_cyclic(decode_cyclic(s)), s)
```
This Python code implements a function called `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. It also defines a `decode_cyclic` function that takes an input string and returns its decoded version. The `assert` statement is used to judge the function's correctness by checking if the encoded string and decoded string are equal.