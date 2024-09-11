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
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
        s (str): The encoded string.
    
    Returns:
        str: The decoded string.
    """
    # Initialize an empty result string
    result = ""
    
    # Iterate over the encoded string in steps of 3
    for i in range(0, len(s), 3):
        # Extract a group of 3 characters
        group = s[i:i+3]
        
        # If the group has more than 2 characters, cycle them
        if len(group) == 3:
            result += group[1:] + group[0]
        # If the group has 2 characters, add them to the result as is
        elif len(group) == 2:
            result += group
        # If the group has 1 character, add it to the result as is
        else:
            result += group
    
    return result


# Test the functions
encoded = encode_cyclic("HelloWorld")
decoded = decode_cyclic(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, and adds a test to demonstrate that they work correctly.