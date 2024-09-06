```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    same sames a same format
    """
    assert encode_cyclic(decode_cyclic(s)) == s
    return decode_cyclic(s)

# Testing the function
test_encode_decode("hello world")
test_encode_decode("hello!world")
test_encode_decode("hello.")
test_encode_decode("heLLoW")
test_encode_decode(".")
test_encode_decode("Python is great!")
```
This code implements a simple encoding and decoding function to solve the problem. It takes an method to split the string into groups of three characters, and then cycles the characters within each group. The decoded string is then returned.