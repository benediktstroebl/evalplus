```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    saw in: it's decrypted.
    """
    test_decoded_cyclic(encode_cyclic('Hello World')))
    assert decode_cyclic('HXLu5fFHeR8uY9cJw5 graders') == 'Hello World'
    assert decode_cyclic('HR8d membrane2 ') == 'Hello World'
    assert decode_cyclic('HXLu5fFHeR8uYf5 graders') == 'Hello World'
    assert decode_cyclic('HXLuY80cY rhin craze') == 'Hello World'
    assert decode_cyclic('HXLu5fHeR8uY8klrauY') == 'Hello World'
    assert decode_cyclic('HXLu5fHXR8uY5 djg=="') == 'Hello World'
```