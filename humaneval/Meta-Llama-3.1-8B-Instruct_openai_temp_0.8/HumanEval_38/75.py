```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    The function works by splitting the input string into groups of three characters.
    If a group has fewer than three characters, it is left unchanged.
    Otherwise, the first character is moved to the end of the group.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    The function works by splitting the input string into groups of three characters.
    If a group has exactly three characters, it is rotated back to its original order.
    Otherwise, the group is left unchanged.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # rotate elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
s = "hello world"
encoded = encode_cyclic(s)
decoded = decode_cyclic(encoded)
print(f"Original string: {s}")
print(f"Encoded string: {encoded}")
print(f"Decoded string: {decoded}")
```

In this script, I completed the `decode_cyclic` function according to your description. Also, I added an example usage section to demonstrate how to use these functions.