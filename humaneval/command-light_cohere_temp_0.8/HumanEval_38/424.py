```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    also returns tests the example that the encoded string is valid."""
    return encode_cyclic(s) == s

# test cases
test_encode_cyclic("Hello World")
test_encode_cyclic("ABCDEFGHIJKLMNOPQRSTUV")
test_encode_cyclic("1234567890abcdefghijklmnopqrstuv")
test_encode_cyclic("ABCDEFGHIJKLMNOPQRSTUVabcde")
test_encode_cyclic("ABCDEFGHIJKLMNOOPQRSTUV")
test_encode_cyclic("ABCDEFGHIJKLMNOOPQRSTUV Abcdef")
test_encode_cyclic("ABCDEFGHIJKLMNOOPQRSTUvw")
test_encode_cyclic("ABCDEFGHIJKLMNOOPQRSTUVabc 123")
test_encode_cyclic("ABCDEFGJKLMNOOPQRSTUV Abcdef 123")
```
The code defines two functions: encode_cyclic and decode_cyclic. The encode_cyclic function encodes a given string using a cyclic group of three characters, and the decode_cyclic function decodes the given string. The code also provides some test cases to verify if the functions are working correctly.