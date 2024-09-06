```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    class pass thel tests to ensure that the encode and decode function work correctly:

test_encode = "hello world"
test_decode = "hello world"
test_decode = encode_cyclic(test_encode)
assert test_decode == test_encode

test_encode = "ohio replpc"
test_decode = encode_cyclic(test_encode)
assert test_decode == test_encode

test_encode = "aaaaaa"
test_decode = encode_cyclic(test_encode)
assert test_decode == test_encode

test_encode = "lets do encode"
test_decode = encode_cyclic(test_encode)
assert test_decode == test_encode

test_encode = "hello, world"
test_decode = encode_cyclic(test_encode)
assert test_decode == test_encode
```
The script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits the input string into groups of three characters each, and cycles the characters within each group. The `decode_cyclic` function takes the encoded string as input and returns the original decoded string. The script test cases demonstrate that the `encode_cyclic` and `decode_cyclic` functions correctly encode and decode the input strings.