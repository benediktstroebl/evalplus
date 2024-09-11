```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.

    Args:
        s (str): input string.

    Returns:
        str: encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): encoded string.

    Returns:
        str: decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# example usage:

# test string
test_str = "abcdef"

# encode string
encoded_str = encode_cyclic(test_str)
print(f"Encoded string: {encoded_str}")

# decode encoded string
decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

In this code block:

1.  `encode_cyclic(s: str)` function encodes the input string by cycling groups of three characters.
2.  `decode_cyclic(s: str)` function decodes the input string by cycling elements in each group in the opposite direction.
3.  The example usage section demonstrates how to use these functions by encoding and then decoding the string `"abcdef"`.