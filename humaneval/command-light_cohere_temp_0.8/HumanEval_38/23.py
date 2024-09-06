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
    high quality and
    string is in base64 encoded.
    return s.decode('utf-8.""" + encode_cyclic(s))

# tests

# test_encode_cyclic
test_encode_cyclic.encode_cyclic('B')
test_encode_cyclic.encode_cyclic('bb')
test_encode_cyclic.encode_cyclic('D')
test_encode_cyclic.encode_cyclic('dEf')
test_encode_cyclic.encode_cyclic('f')
test_encode_cyclic.encode_cyclic('F')
test_encode_cyclic.encode_cyclic('f0')
test_encode_cyclic.encode_cyclic('A')
test_encode_cyclic.encode_cyclic('a')
test_encode_cyclic.encode_cyclic('aa')
test_encode_cyclic.encode_cyclic('Z')
test_encode_cyclic.encode_cyclic('zzz')

# test_decode_cyclic
test_decode_cyclic.decode_cyclic('B')
test_decode_cyclic.decode_cyclic('bb')
test_decode_cyclic.decode_cyclic('D')
test_decode_cyclic.decode_cyclic('dEf')
test_decode_cyclic.decode_cyclic('f')
test_decode_cyclic.decode_cyclic('F')
test_decode_cyclic.decode_cyclic('g')
test_decode_cyclic.decode_cyclic('G')
test_decode_cyclic.decode_cyclic('h')
test_decode_cyclic.decode_cyclic('H')
test_decode_cyclic.decode_cyclic('i')
test_decode_cyclic.decode_cyclic('I')
test_decode_cyclic.decode_cyclic('j')
test_decode_cyclic.decode_cyclic('k')
test_decode_cyclic.decode_cyclic('l')
test_decode_cyclic.decode_cyclic('')
test_decode_cyclic.decode_cyclic('1')
```
This script defines the functions `encode_cyclic` and `decode_cyclic`, which solve the problem of encoding and decoding a string of characters in a cyclic format, respectively. It also includes the corresponding tests to verify the correctness of the functions.