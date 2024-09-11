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
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# test the functions
input_str = "abcdefghi"
encoded_str = encode_cyclic(input_str)
decoded_str = decode_cyclic(encoded_str)

print("Input string:", input_str)
print("Encoded string:", encoded_str)
print("Decoded string:", decoded_str)
```

This script defines `encode_cyclic` and `decode_cyclic` functions according to your problem description. The `encode_cyclic` function cycles elements in groups of three, while the `decode_cyclic` function reverses this operation. The script then tests these functions on the input string `"abcdefghi"`.