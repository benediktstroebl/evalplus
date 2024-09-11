```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): Input encoded string.
    
    Returns:
    str: Decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Decoded group is empty if original group had fewer than 3 characters
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            decoded_groups.append(group[-1] + group[0] + group[1])
        else:
            decoded_groups.append(group)
    return "".join(decoded_groups)


# Example usage
original_string = "HelloWorld"
encoded_string = encode_cyclic(original_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles the characters in each group (unless the group has fewer than three characters), and returns the encoded string. The `decode_cyclic` function reverses the process, splitting the encoded string back into groups, cycling the characters in each group (if necessary), and returning the decoded string.

Note: If the original string has a length that is not divisible by 3, the last group will have fewer than three characters. In this case, the `encode_cyclic` function will leave the last group unchanged, and the `decode_cyclic` function will insert an empty string at the end of the decoded string to maintain the original length.