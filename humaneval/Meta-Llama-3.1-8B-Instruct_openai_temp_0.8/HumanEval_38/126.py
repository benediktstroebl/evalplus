### Cyclic Encoding and Decoding
#### Problem Description

The following Python script provides a solution to the cyclic encoding and decoding problem. It introduces two functions: `encode_cyclic` and `decode_cyclic`. These functions work in tandem to first encode a given string into a cyclically rearranged format, and then decode the encoded string back to its original format.

```python
def encode_cyclic(s: str):
    """
    Returns the encoded string by cycling groups of three characters.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string into groups of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group, unless the group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function and returns the decoded string.

    :param s: Input encoded string
    :return: Decoded string
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over the characters in the encoded string
    for char in s:
        # Add the character to the current group
        current_group += char
        
        # If the current group has length 3, add it to the decoded groups and reset the current group
        if len(current_group) == 3:
            decoded_groups.append(current_group)
            current_group = ""
    
    # If there's a remaining character in the current group, add it to the decoded groups
    if current_group:
        decoded_groups.append(current_group)
    
    # Initialize an empty string to store the decoded string
    decoded_string = ""
    
    # Iterate over the decoded groups
    for group in decoded_groups:
        # If the group has length 3, cycle its elements
        if len(group) == 3:
            decoded_string += group[1:] + group[0]
        # If the group has fewer elements than 3, keep its original order
        else:
            decoded_string += group
    
    # Return the decoded string
    return decoded_string


# Example usage
input_string = "abcdefgh"
encoded_string = encode_cyclic(input_string)
decoded_string = decode_cyclic(encoded_string)

print(f"Input string: {input_string}")
print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

This script includes two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and then cycles the elements in each group. The `decode_cyclic` function takes an encoded string as input, splits it into groups, and then decodes each group by cycling its elements. The example usage demonstrates how to use these functions to encode and decode a string.