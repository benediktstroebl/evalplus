### Cyclic Encoding and Decoding
#### Problem Description

This script implements two functions, `encode_cyclic` and `decode_cyclic`, to cycle groups of three characters in a string and their corresponding decoding function.

#### Code

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The encoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join groups into a single string.
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store decoded groups.
    decoded_groups = []
    
    # Initialize an empty string to store the current group.
    group = ""
    
    # Iterate over the input string.
    for char in s:
        # Add the current character to the group.
        group += char
        
        # If the group has 3 characters, add it to the decoded groups and reset the group.
        if len(group) == 3:
            decoded_groups.append(group)
            group = ""
    
    # If there are remaining characters in the group, add them to the decoded groups.
    if group:
        decoded_groups.append(group)
    
    # Initialize an empty string to store the decoded string.
    decoded_string = ""
    
    # Iterate over the decoded groups.
    for i, group in enumerate(decoded_groups):
        # If the group has more than 3 characters, cycle them.
        if len(group) > 3:
            decoded_string += group[-1] + group[1:-1] + group[0]
        # If the group has 3 characters, cycle them.
        elif len(group) == 3:
            decoded_string += group[1:] + group[0]
        # If the group has fewer characters than 3, add them as is.
        else:
            decoded_string += group
    
    # Return the decoded string.
    return decoded_string


# Example usage
if __name__ == "__main__":
    s = "abcdefghi"
    encoded = encode_cyclic(s)
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")
```

#### Explanation

The `encode_cyclic` function splits the input string into groups of three characters. If a group has fewer than three characters, it is left as is. Otherwise, the last character is moved to the beginning of the group. The groups are then joined together to form the encoded string.

The `decode_cyclic` function splits the input string into groups. If a group has more than three characters, the last character is moved to the beginning of the group. If a group has three characters, the last character is moved to the beginning of the group. If a group has fewer than three characters, it is left as is. The groups are then joined together to form the decoded string.