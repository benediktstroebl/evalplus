### Cyclic Encoding and Decoding Script
```markdown
### Problem Description
This script provides two functions: `encode_cyclic` and `decode_cyclic`. 
`encode_cyclic` takes a string, splits it into groups of three characters, 
and cycles the elements in each group (unless the group has fewer than three elements). 
The result is returned as a string. 
`decode_cyclic` is the reverse operations, taking an encoded string and returning the original string.

### Code
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    # Initialize an empty string to build each group
    group = ""
    # Iterate over the input string
    for char in s:
        # Add the character to the current group
        group += char
        # If the group has three characters, add it to the decoded groups and reset the group
        if len(group) == 3:
            # If the group has three characters, cycle them
            if len(group) == 3:
                decoded_groups.append(group[1:] + group[0])
            else:
                decoded_groups.append(group)
            group = ""
    # If there's a remaining group, add it to the decoded groups
    if group:
        # If the group has three characters, cycle them
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        else:
            decoded_groups.append(group)
    
    # Join the decoded groups to form the decoded string
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    original_string = "ababab"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Explanation

The `encode_cyclic` function splits the input string into groups of three characters, 
cycles the elements in each group (unless the group has fewer than three elements), 
and returns the encoded string.

The `decode_cyclic` function takes an encoded string, rebuilds the original groups, 
cycles the elements in each group (if necessary), and returns the decoded string.

Both functions handle edge cases where the input string has a length that is not a multiple of 3.