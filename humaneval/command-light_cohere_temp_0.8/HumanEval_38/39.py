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
    takes as input string encoded with encode_cyclic function. Returns decoded string
    performed by the encode_cyclic function.
    """
    pass the test encode_cyclic("hello")
    # it should return "oenheddoelro"
    print(decode_cyclic("olenheddoelro"))
    # it should return "hello"
    print(decode_cyclic("h corro "))
    # it should return "h corro "
    print(decode_cyclic("hello"))
```