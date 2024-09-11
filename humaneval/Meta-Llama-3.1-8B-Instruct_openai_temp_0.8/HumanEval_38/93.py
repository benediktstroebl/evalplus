```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split string to groups of length 3. 
    # Use padding with spaces if the length of the string is not a multiple of 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] + " " * (3 - len(s) % 3) for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 4 else group for group in groups]
    
    # Remove trailing spaces before joining the groups
    groups = [group.rstrip() for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with the encode_cyclic function. 
    Returns the decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Convert the string into a list of characters
    char_list = list(s)
    
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Initialize an empty string to store the current group
    group = ""
    
    # Iterate over the characters in the string
    for char in char_list:
        # If the character is a space, it means we've reached the end of a group
        if char == " ":
            # Add the current group to the list of decoded groups
            decoded_groups.append(group)
            # Reset the current group
            group = ""
        else:
            # Add the character to the current group
            group += char
    
    # Handle the last group (which might not be followed by a space)
    if group:
        # If the group has 3 characters, cycle them; otherwise, leave it as is
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        else:
            decoded_groups.append(group)
    
    # Join the decoded groups into a string and return the result
    return "".join(decoded_groups)


# Example usage
encoded_string = encode_cyclic("abcdefgh")
print(f"Encoded string: {encoded_string}")
decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```