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
    # split string to groups
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode groups by moving first character to end
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
encoded_str = encode_cyclic("abcdef")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script uses list comprehension to split the input string into groups of three characters and then cycle the elements in each group to encode the string. The `decode_cyclic` function reverses this process to decode the string back to its original form.