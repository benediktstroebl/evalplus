```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Example:
    >>> encode_cyclic("abcdef")
    'efabcd'
    
    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Example:
    >>> decode_cyclic("efabcd")
    'abcdef'
    
    :param s: Input encoded string to be decoded.
    :return: Decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    # Initialize a temporary group
    temp_group = []
    
    # Iterate over characters in the encoded string
    for char in s:
        # Add character to the temporary group
        temp_group.append(char)
        # If the temporary group has 3 characters, add it to decoded groups and reset the temporary group
        if len(temp_group) == 3:
            decoded_groups.append(temp_group)
            temp_group = []
    
    # Handle the case when the encoded string has fewer than 3 characters
    if temp_group:
        # If the temporary group has exactly 2 characters, add it to decoded groups with a dummy character '0' prepended
        if len(temp_group) == 2:
            decoded_groups.append('0' + ''.join(temp_group))
        # If the temporary group has exactly 1 character, add it to decoded groups with two dummy characters '00' prepended
        elif len(temp_group) == 1:
            decoded_groups.append('00' + temp_group[0])
    
    # Decode the groups
    decoded = []
    for group in decoded_groups:
        # If the group has 3 characters, decode it as is
        if len(group) == 3:
            decoded.append(group)
        # If the group has 2 characters, prepend a dummy character and decode it
        elif len(group) == 2:
            decoded.append('0' + group)
        # If the group has 1 character, prepend two dummy characters and decode it
        elif len(group) == 1:
            decoded.append('00' + group)
    
    # Join the decoded groups into a single string
    return ''.join([group[1] + group[0] if len(group) > 1 else group[0] for group in decoded])


# Test the functions
print(encode_cyclic("abcdef"))
print(decode_cyclic("efabcd"))
```