### Cyclic Encoding and Decoding Script

Below is a Python script that encodes and decodes a string by cycling groups of three characters.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # Split string into groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless the group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes an encoded string from the encode_cyclic function and returns the decoded string.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Initialize an empty list to store the decoded groups.
    decoded_groups = []
    
    # Initialize an empty string to build each group of three characters.
    group = ""
    
    # Iterate over each character in the encoded string.
    for char in s:
        # Add the character to the current group.
        group += char
        
        # If the group has three characters, add it to the decoded groups and reset the group.
        if len(group) == 3:
            decoded_groups.append(group)
            group = ""
    
    # If there are remaining characters in the last group, add them to the decoded groups.
    if group:
        decoded_groups.append(group)
    
    # Initialize an empty string to build the decoded string.
    decoded_string = ""
    
    # Iterate over each decoded group.
    for i, group in enumerate(decoded_groups):
        # If the group has three characters, cycle the characters to prepare for decoding.
        if len(group) == 3:
            decoded_string += group[1:] + group[0]
        # If the group has fewer than three characters, add it to the decoded string as is.
        else:
            decoded_string += group
        
        # If it's not the last group, add a space before the next group.
        if i < len(decoded_groups) - 1:
            decoded_string += " "
    
    return decoded_string


# Example usage:
if __name__ == "__main__":
    # Test string
    test_string = "abcdefghij"
    
    # Encode the test string
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")
    
    # Decode the encoded string
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles the characters in each group (unless the group has fewer than three characters), and returns the encoded string. The `decode_cyclic` function takes the encoded string, splits it into groups, and cycles the characters back to their original order to produce the decoded string.

In the example usage section, we test the encoding and decoding functions with a sample string.