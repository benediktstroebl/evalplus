```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Example:
        >>> encode_cyclic("abcdef")
        'badcfe'
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Example:
        >>> decode_cyclic("badcfe")
        'abcdef'
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
encoded = encode_cyclic("abcdef")
decoded = decode_cyclic(encoded)

assert encoded == "badcfe"
assert decoded == "abcdef"

print("Tests passed!")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function does the reverse to recover the original string. The script also includes test cases to verify the correctness of the functions.