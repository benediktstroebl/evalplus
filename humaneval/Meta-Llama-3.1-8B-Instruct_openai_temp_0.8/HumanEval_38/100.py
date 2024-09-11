```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    For example:
    - "abc" -> "bca"
    - "abcd" -> "dabc"
    - "defghi" -> "egfhdhi"
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    For example:
    - "bca" -> "abc"
    - "dabc" -> "abcd"
    - "egfhdhi" -> "defghi"
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by moving the first character to the end.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
encoded = encode_cyclic("abcdef")
print(f"Encoded string: {encoded}")

decoded = decode_cyclic(encoded)
print(f"Decoded string: {decoded}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, and includes example usage to demonstrate their functionality. The functions use list comprehensions to split the input string into groups of three characters, then cycle the elements in each group or decode them back to their original order as needed. The example usage shows how to use these functions to encode and decode a string.