### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: The input string to be decoded.
    :return: The decoded string.
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the encoded string
    for char in s:
        # Add the character to the current group
        current_group += char
        
        # If the current group has 3 characters, add it to the list and reset it
        if len(current_group) == 3:
            # If the current group has more than 3 characters, remove the first one
            if len(current_group) > 3:
                current_group = current_group[1:]
            decoded_groups.append(current_group)
            current_group = ""
    
    # If there are remaining characters in the current group, add them to the list
    if current_group:
        decoded_groups.append(current_group)
    
    # Decode the groups by taking the first character and moving it to the end
    decoded_groups = [group[1:] + group[0] if len(group) == 3 else group for group in decoded_groups]
    
    # Join the decoded groups into a single string
    decoded_string = "".join(decoded_groups)
    
    return decoded_string


# Example usage:
if __name__ == "__main__":
    encoded_string = encode_cyclic("abcdef")
    print("Encoded string:", encoded_string)
    
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
```
This script provides the `encode_cyclic` function to encode a string by cycling groups of three characters, and the `decode_cyclic` function to decode a string encoded with `encode_cyclic`. The example usage demonstrates the encoding and decoding of the string "abcdef".