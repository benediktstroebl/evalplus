Here's a self-contained Python script that solves the problem in a markdown code block:

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string with groups of three characters cycled.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): Encoded string.
    
    Returns:
    str: Decoded string.
    """
    # decode string by cycling groups of three characters in reverse
    decoded_groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in decoded_groups]
    return "".join(decoded_groups)


# Test the functions
s = "abcdefg"
encoded = encode_cyclic(s)
print(f"Encoded string: {encoded}")

decoded = decode_cyclic(encoded)
print(f"Decoded string: {decoded}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement the described behavior. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group (unless the group has fewer than three characters), and returns the encoded string. The `decode_cyclic` function takes an encoded string as input, reverses the cycling of groups, and returns the decoded string. The script also includes a test case to demonstrate the usage of the functions.