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
    # reverse cycle in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghi"
    encoded = encode_cyclic(original_string)
    print(f"Encoded string: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded string: {decoded}")
```

In this code:

- The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group (unless it has fewer than three characters), and joins the groups back into a single string.
- The `decode_cyclic` function performs the reverse operation: it splits the input string into groups, reverses the cycling in each group (by prepending the last character to the rest), and joins the groups back into a single string.
- The example usage in the `if __name__ == "__main__":` block demonstrates how to use these functions to encode and decode a string.