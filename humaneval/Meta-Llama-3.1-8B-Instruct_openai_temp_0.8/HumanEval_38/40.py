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
    # If the length of the string is less than 3, return it as it is because we cannot split it into groups of 3
    if len(s) < 3:
        return s
    
    # Split the string into groups of 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    
    # Iterate over each group
    for group in groups:
        # If the group has 3 characters, cycle them to get the decoded group
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        # If the group has less than 3 characters, it is the last group of the encoded string, so add it to the decoded groups as it is
        else:
            decoded_groups.append(group)
    
    # Join the decoded groups into a string and return it
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefghi")
    print("Encoded string:", encoded_str)
    decoded_str = decode_cyclic(encoded_str)
    print("Decoded string:", decoded_str)
```

The `decode_cyclic` function has been implemented as per the given requirements. It first checks if the length of the string is less than 3 and returns it as it is. Then it splits the string into groups of 3 and iterates over each group. If a group has 3 characters, it cycles them to get the decoded group. If a group has less than 3 characters, it is the last group of the encoded string, so it adds it to the decoded groups as it is. Finally, it joins the decoded groups into a string and returns it.