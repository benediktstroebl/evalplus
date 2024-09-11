### Cyclic Encoding and Decoding in Python

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split string to groups of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group unless the group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function and returns decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over the characters in the input string
    for char in s:
        # Add the character to the current group
        current_group += char
        
        # If the current group has 3 characters, add it to the list of decoded groups and reset the current group
        if len(current_group) == 3:
            decoded_groups.append(current_group)
            current_group = ""
    
    # If there are any remaining characters in the current group, add them to the list of decoded groups
    if current_group:
        decoded_groups.append(current_group)
    
    # Decode each group by cycling its elements
    decoded_groups = [decode_group(group) for group in decoded_groups]
    
    return "".join(decoded_groups)

def decode_group(group: str) -> str:
    """
    Decodes a group of three characters by cycling its elements.
    
    Args:
    group (str): The group of three characters to be decoded.
    
    Returns:
    str: The decoded group.
    """
    # If the group has fewer than 3 characters, return its reversed version
    if len(group) < 3:
        return group[::-1]
    
    # Otherwise, return the group with its first element moved to the end
    return group[1:] + group[0]

# Example usage:
encoded = encode_cyclic("abcdefgh")
print(f"Encoded: {encoded}")

decoded = decode_cyclic(encoded)
print(f"Decoded: {decoded}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string, splits it into groups, decodes each group, and returns the original string. The `decode_group` function is a helper function used by `decode_cyclic` to decode a single group of three characters.