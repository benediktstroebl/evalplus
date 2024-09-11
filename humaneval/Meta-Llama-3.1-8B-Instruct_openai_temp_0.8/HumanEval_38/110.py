### Cyclic Encoding and Decoding

The following Python script contains functions to encode and decode a string by cycling groups of three characters.

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
    # Initialize an empty string to store the decoded result
    decoded_string = ""
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in s:
        # Add the character to the current group
        current_group += char
        
        # If the length of the current group is 3, add it to the decoded string and reset the group
        if len(current_group) == 3:
            if len(current_group) == 2:
                decoded_string += current_group + "X"
            else:
                decoded_string += current_group[1] + current_group[0] + current_group[2]
            current_group = ""
    
    # If there are remaining characters in the current group, add them to the decoded string
    if current_group:
        if len(current_group) == 2:
            decoded_string += current_group + "X"
        else:
            decoded_string += current_group[1] + current_group[0]
    
    return decoded_string


# Example usage
if __name__ == "__main__":
    input_string = "abcdef"
    encoded_string = encode_cyclic(input_string)
    print("Encoded string:", encoded_string)
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
```

This script first defines the `encode_cyclic` function to encode a string by cycling groups of three characters. It then defines the `decode_cyclic` function to decode a string that was encoded using `encode_cyclic`. Finally, it provides an example usage of these functions.