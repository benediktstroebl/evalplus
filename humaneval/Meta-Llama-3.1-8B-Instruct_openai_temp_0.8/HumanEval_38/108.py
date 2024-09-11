### Cyclic Encoding and Decoding
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
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over the characters in the encoded string
    for char in s:
        current_group += char
        
        # If the current group has 3 characters, add it to the decoded groups and reset it
        if len(current_group) == 3:
            if len(current_group[1:]) >= 1 and len(current_group[:1]) >= 1:
                decoded_groups.append(current_group[1:] + current_group[0])
            else:
                decoded_groups.append(current_group)
            current_group = ""
    
    # If there are any remaining characters in the current group, add them to the decoded groups
    if current_group:
        if len(current_group[1:]) >= 1 and len(current_group[:1]) >= 1:
            decoded_groups.append(current_group[1:] + current_group[0])
        else:
            decoded_groups.append(current_group)
    
    # Join the decoded groups into a single string and return it
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    encoded_string = encode_cyclic("abcdefg")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this code, the `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and joins them into a single string. The `decode_cyclic` function works in reverse by iterating over the characters in the encoded string, grouping them into sets of three, and cycling the elements in each group to reconstruct the original string. The example usage demonstrates how to use these functions to encode and decode a string.