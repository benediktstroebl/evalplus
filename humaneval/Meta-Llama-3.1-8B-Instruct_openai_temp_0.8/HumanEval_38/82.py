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
    # split string to groups. Each of length 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # decode elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
encoded_str = encode_cyclic("HelloWorld")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script includes the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the characters in each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string as input, splits it into groups of three characters, decodes the groups by cycling the characters, and returns the decoded string. The script also includes an example usage to demonstrate how to use these functions.