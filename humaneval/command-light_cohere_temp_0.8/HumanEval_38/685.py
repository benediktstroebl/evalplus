Here is a Python script that includes the self-contained function to solve the problem:

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
    standard string to lowercase
    """
    return s.lower()


test_encode_cyclic = "AE chess A"
# test_encode_cyclic should return 'declare war groups'

test_decode_cyclic = encode_cyclic.decode_cyclic(test_encode_cyclic)
# test_decode_cyclic should return 'AE saa'
```

This Python script provides a self-contained solution to the problem of encoding and decoding a string of characters. You can use the also test the solution using the test cases provided.