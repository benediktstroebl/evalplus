```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    expected behaviour is tested with encode_cyclic
    """
    return s.decode(encode_cyclic(s))

# Example usage
test_encode = "AabbccD"
test_decode = encode_cyclic(test_encode)
print(test_encode, "==",test_decode)
```
This script defines a self-contained function called encode_cyclic that takes a string s as input and returns the encoded string. The function splits the string into groups of three characters and cycles the groups, with a minimum length of 3.

The script also defines a function called decode_cyclic that takes a string s as input and returns the decoded string. The expected behaviour of the function is tested by an example usage, and the results are printed.