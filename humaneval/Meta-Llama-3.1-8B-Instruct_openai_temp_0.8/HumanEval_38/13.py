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
    # reverse cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
s = "abcdefgh"
encoded = encode_cyclic(s)
decoded = decode_cyclic(encoded)

print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions to encode and decode a string by cycling groups of three characters. The `encode_cyclic` function splits the string into groups of three characters, then cycles the elements in each group by moving the first element to the end. The `decode_cyclic` function reverses this process by moving the last element to the beginning. The example usage at the end demonstrates how to use these functions to encode and decode a string.