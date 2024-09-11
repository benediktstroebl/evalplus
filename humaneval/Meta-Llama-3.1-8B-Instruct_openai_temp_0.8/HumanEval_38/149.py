### Cyclic Encoding and Decoding Script
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
    s (str): Input encoded string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Initialize an empty string to build each group
    group = ""
    
    # Iterate over the characters in the encoded string
    for char in s:
        # Add the character to the current group
        group += char
        
        # If the group has 3 characters, add it to the list of decoded groups
        if len(group) == 3:
            if len(group) == 1:
                decoded_groups.append(group)
            else:
                decoded_groups.append(group[1:] + group[0])
            # Reset the group
            group = ""
    
    # If there are remaining characters in the group, add them to the list of decoded groups
    if group:
        if len(group) == 1:
            decoded_groups.append(group)
        else:
            decoded_groups.append(group[1:] + group[0])
    
    # Join the decoded groups into a single string and return it
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefgh")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes an input string and encodes it by cycling groups of three characters. The `decode_cyclic` function takes an input string encoded with `encode_cyclic` and decodes it back to the original string.

The example usage at the end demonstrates how to use these functions to encode and decode a string.