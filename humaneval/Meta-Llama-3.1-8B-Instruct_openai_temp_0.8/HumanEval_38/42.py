### Cyclic Encoding and Decoding
#### Problem Solution

Below is a Python script that defines the `encode_cyclic` and `decode_cyclic` functions as specified.

```markdown
### Code
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string.
    :return: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string.
    :return: Decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Initialize an empty string to build current group
    current_group = ""
    
    # Iterate over the input string
    for char in s:
        # Add character to the current group
        current_group += char
        
        # If the current group has 3 characters, add it to the decoded groups and reset the current group
        if len(current_group) == 3:
            # If the current group has more than 3 characters (which is impossible, but to be safe)
            if len(current_group) > 3:
                # Remove the last character from the current group
                current_group = current_group[:-1]
            decoded_groups.append(current_group)
            current_group = ""
    
    # If there are any remaining characters in the current group, add them to the decoded groups
    if current_group:
        # If the current group has more than 3 characters (which is impossible, but to be safe)
        if len(current_group) > 3:
            # Remove the last character from the current group
            current_group = current_group[:-1]
        decoded_groups.append(current_group)
    
    # If the decoded groups list is empty (which is impossible, but to be safe)
    if not decoded_groups:
        return ""
    
    # Initialize an empty list to store final decoded characters
    final_chars = []
    
    # Iterate over the decoded groups
    for group in decoded_groups:
        # If the group has 3 characters, cycle them
        if len(group) == 3:
            final_chars.append(group[1:] + group[0])
        # If the group has less than 3 characters, leave them as is
        else:
            final_chars.append(group)
    
    # Return the decoded string
    return "".join(final_chars)
```

#### Example Usage

```markdown
# Encode a string
encoded_str = encode_cyclic("abcdefgh")
print("Encoded string:", encoded_str)

# Decode the string
decoded_str = decode_cyclic(encoded_str)
print("Decoded string:", decoded_str)
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified. The `encode_cyclic` function splits the input string into groups of 3 characters, cycles the characters in each group (unless the group has fewer than 3 characters), and joins the grouped and cycled characters into a single string. The `decode_cyclic` function takes the encoded string, splits it into groups, cycles the characters in each group (unless the group has fewer than 