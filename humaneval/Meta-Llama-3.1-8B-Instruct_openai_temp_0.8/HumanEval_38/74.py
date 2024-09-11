```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split encoded string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group. If group has fewer elements than 3, add the first element at the end.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
original_string = "HelloWorldThisIsATest"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

In this script, we first define the `encode_cyclic` function, which takes a string `s` as input and encodes it by cycling groups of three characters. We then define the `decode_cyclic` function, which takes an encoded string as input and decodes it by reversing the process used in the `encode_cyclic` function. Finally, we test the functions by encoding an original string and then decoding the encoded string to ensure that the original string is recovered.