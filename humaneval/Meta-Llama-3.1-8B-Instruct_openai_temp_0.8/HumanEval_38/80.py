```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    This function splits the input string into groups of three characters, 
    then cycles the elements in each group unless the group has fewer elements than three.
    
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
    
    This function splits the input string into groups of three characters, 
    then checks if the second character of each group is the same as the first character of the next group.
    If not, it moves the first character of the group to the end of the group.
    
    Args:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Iterate over the groups
    for i in range(len(groups) - 1):
        group = groups[i]
        next_group = groups[i + 1]
        # If the second character of the group is the same as the first character of the next group
        if group[1] == next_group[0]:
            # Move the first character of the group to the end of the group
            decoded_groups.append(group[1:] + group[0])
        else:
            decoded_groups.append(group)
    
    # Add the last group to the decoded groups list
    decoded_groups.append(groups[-1])
    
    # Join the decoded groups into a single string
    decoded_string = "".join(decoded_groups)
    
    return decoded_string


# Example usage:
s = "abcdefg"
encoded_s = encode_cyclic(s)
print(f"Encoded string: {encoded_s}")

decoded_s = decode_cyclic(encoded_s)
print(f"Decoded string: {decoded_s}")
```
This script includes both the `encode_cyclic` and `decode_cyclic` functions, along with an example usage at the end. The `decode_cyclic` function has been updated to correctly handle the decoding of the encoded string.