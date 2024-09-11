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
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Loop through the length of the input string in steps of 3
    for i in range(0, len(s), 3):
        # If the current index plus 2 is greater than the length of the string, 
        # then we have a group of less than 3 characters
        if i + 2 >= len(s):
            # In this case, we just append the group to the decoded groups list
            decoded_groups.append(s[i:])
        else:
            # Otherwise, we cycle the elements in the group
            group = s[i:i + 3]
            # If the group has fewer than 3 characters, we leave it as is
            if len(group) < 3:
                decoded_groups.append(group)
            # Otherwise, we cycle the elements in the group
            else:
                decoded_groups.append(group[1:] + group[0])
    
    # Join the decoded groups into a single string
    decoded_string = "".join(decoded_groups)
    
    return decoded_string


# Test the functions
encoded = encode_cyclic("abcdefgh")
decoded = decode_cyclic(encoded)

print("Encoded string: ", encoded)
print("Decoded string: ", decoded)
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, that implement the described cyclic encoding and decoding logic. The `encode_cyclic` function splits the input string into groups of 3 characters and cycles the elements in each group. The `decode_cyclic` function reverses this process to obtain the original string. The script also includes test cases to demonstrate the functionality of the functions.