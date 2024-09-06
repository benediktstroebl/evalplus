```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    universal encoding and encoding cycle with three characters
    """
    return s.decode(groups)

# encode and decode test cases

encoded_test = encode_cyclic("Hello World")
print("Encoded:", encoded_test)

decoded_test = decode_cyclic(encoded_test)
print("Decoded:", decoded_test)
```

This Python script defines a self-contained function to solve the problem of encoding and decoding markdown code with a cyclic group of three characters. The encode_cyclic function splits the input string into groups of three characters, cycles each group elements, and returns the result as a string. The function also handles the case where a group has fewer elements than three by returning the group as it is. The decode_cyclic function takes the encoded string as input, decodes it using the groups returned by the encode_cyclic function, and returns the decoded string.