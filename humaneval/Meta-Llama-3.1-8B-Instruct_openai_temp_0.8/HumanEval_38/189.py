```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = []
    for i in range((len(s) + 2) // 3):
        start = 3 * i
        end = min((3 * i + 3), len(s))
        group = s[start:end]
        # Cycle elements in each group. Unless group has fewer elements than 3.
        if len(group) == 3:
            group = group[1:] + group[0]
        groups.append(group)
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
        s (str): The encoded string.
    
    Returns:
        str: The decoded string.
    """
    result = []
    i = 0
    while i < len(s):
        # Check for groups of length 2 and length 3
        if i + 2 < len(s):
            # Group of length 3
            if i + 3 <= len(s):
                group = s[i:i+3]
                result.append(group[1:] + group[0])
            # Group of length 2
            else:
                group = s[i:i+2]
                result.append(group[1] + group[0])
            i += 3
        elif i + 1 < len(s):
            # Group of length 2
            group = s[i:i+2]
            result.append(group[1] + group[0])
            i += 2
        else:
            # If only one character left, just append it
            result.append(s[i])
            i += 1
    return "".join(result)


# Test the functions
s = "abcdefgh"
encoded = encode_cyclic(s)
print(f"Encoded string: {encoded}")
decoded = decode_cyclic(encoded)
print(f"Decoded string: {decoded}")
```

This Python script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group (except for groups with fewer than three characters), and returns the encoded string. The `decode_cyclic` function takes an encoded string as input, identifies the groups of three characters, and decodes the string by cycling the elements in each group. The script also includes a test case to demonstrate the usage of these functions.