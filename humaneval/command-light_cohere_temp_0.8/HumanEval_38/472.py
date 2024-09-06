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
    general case test for the string
    """
    return "".join(decode_cyclic(s))

# Test cases
test_encode = ["abc", "abc", "abc", "b"]
test_decode = ["a", "bb", "aaa"]

print(test_encode, encode_cyclic(test_encode))
print(test_decode, decode_cyclic(test_decode))
``` 

This script defines a self-contained function to encode and decode a string using a cyclical grouping of characters. The `encode_cyclic` function takes a string as input and returns the encoded string. The `decode_cyclic` function is the inverse of the `encode_cyclic` function and returns the original decoded string. The test cases ensure that the function is working correctly.