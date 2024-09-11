### Cyclic Encoding and Decoding

Below is a Python script with the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string with cyclic groups of three characters.
    """
    # Initialize an empty list to store the encoded groups
    encoded_groups = []
    
    # Loop through the string in steps of 3
    for i in range((len(s) + 2) // 3):
        # Get the current group of 3 characters, or the remaining characters if the string length is not a multiple of 3
        group = s[(3 * i):min((3 * i + 3), len(s))]
        
        # If the group has 3 characters, cycle them by moving the first character to the end
        if len(group) == 3:
            encoded_groups.append(group[1:] + group[0])
        # If the group has fewer than 3 characters, leave it as is
        else:
            encoded_groups.append(group)
    
    # Join the encoded groups into a single string
    return "".join(encoded_groups)


def decode_cyclic(s: str):
    """
    Decodes a string that was encoded with the encode_cyclic function.
    
    Args:
        s (str): The encoded string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Loop through the encoded string in steps of 3
    for i in range((len(s) + 2) // 3):
        # Get the current group of 3 characters
        group = s[(3 * i):min((3 * i + 3), len(s))]
        
        # If the group has 3 characters, check if the first character should be moved to the end
        if len(group) == 3 and group[0] == group[2]:
            decoded_groups.append(group[1] + group[0] + group[2])
        # If the group has fewer than 3 characters, leave it as is
        else:
            decoded_groups.append(group)
    
    # Join the decoded groups into a single string
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    # Test string
    test_string = "abcdefghi"
    
    # Encode the string
    encoded_string = encode_cyclic(test_string)
    print("Encoded string:", encoded_string)
    
    # Decode the string
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)

    # Check if the decoded string matches the original string
    if decoded_string == test_string:
        print("Decoding was successful!")
    else:
        print("Decoding failed.")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions, which encode and decode a string by cycling groups of three characters. The `encode_cyclic` function splits the input string into groups of three characters, cycles each group (unless it has fewer than three characters), and joins the groups into a single string. The `decode_cyclic` function reverses this process by checking if each group should be cycled and adjusting it accordingly. The script includes an example usage section to demonstrate the functions' behavior.