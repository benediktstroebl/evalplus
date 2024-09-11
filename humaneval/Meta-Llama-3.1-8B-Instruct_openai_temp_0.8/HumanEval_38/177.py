### Cyclic Coding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Encode a string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split the string into groups of three characters each
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group if it has at least three characters
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decode a string encoded with the encode_cyclic function.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    decoded_string = ""
    i = 0
    
    # Loop through the encoded string in steps of 3
    while i < len(s):
        group = s[i:i+3]
        
        # If the group has 3 characters, cycle them
        if len(group) == 3:
            decoded_string += group[1:] + group[0]
        else:
            # If the group has less than 3 characters, just append it
            decoded_string += group
        
        i += 3
    
    return decoded_string


# Example usage
if __name__ == "__main__":
    encoded_string = encode_cyclic("abcdef")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this code, the `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group if it has at least three characters, and then joins the groups into a single string.

The `decode_cyclic` function decodes a string encoded with `encode_cyclic`. It does this by looping through the encoded string in steps of three, cycling any groups of three characters, and appending any groups with less than three characters to the decoded string.

In the example usage section, we demonstrate how to use these functions by encoding the string "abcdef" and then decoding the result.