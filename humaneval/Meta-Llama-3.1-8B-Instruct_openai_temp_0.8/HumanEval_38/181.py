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
    # split encoded string to groups
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group to get original order
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    # join groups together to form decoded string
    return "".join(groups)


# example usage
if __name__ == "__main__":
    encoded = encode_cyclic("abcdef")
    print(f"Encoded: {encoded}")

    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")
```

This script first defines the `encode_cyclic` function which cyclically shifts characters in groups of three to encode the input string. The `decode_cyclic` function is then defined, which reverses the encoding process by shifting group elements in the opposite direction.

In the example usage section, we can see how to use these functions. We encode the string "abcdef" and then decode the result to confirm that it is the original string.