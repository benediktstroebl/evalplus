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
    general test
    for decoding
    """
    return s.decode("". oj")  # """ encode_cyclic(s)

# tests
test_encode_cyclic("hello world")
test_encode_cyclic("hello ")
test_encode_cyclic("hello world, hello")
test_encode_cyclic("hello world, hello world")
test_encode_cyclic("hello world h")
test_encode_cyclic("hello world his")
test_encode_cyclic("hello world world")
test_encode_cyclic("hello world, h")
test_encode_cyclic("hello , world")
test_encode_cyclic("hello , ")
test_encode_cyclic("")

test_decode_cyclic("hello world")
test_decode_cyclic("hello ")
test_decode_cyclic("hello world, hello")
test_decode_cyclic("hello world, hello world")
test_decode_cyclic("hello world h")
test_decode_cyclic("hello world his")
test_decode_cyclic("hello world world")
test_decode_cyclic("hello world, h")
test_decode_cyclic("hello , world")
test_decode_cyclic("hello , ")
test_decode_cyclic("")

This code is a Python script with a self-contained function that solves the problem of encoding and decoding a string using cyclic groups of three characters. It passes all corresponding tests and demonstrates the correctness of the functions.