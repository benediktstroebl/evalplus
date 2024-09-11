```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Example:
        >>> encode_cyclic("abcabcabc")
        'bcabcabcabc'
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Example:
        >>> decode_cyclic("bcabcabcabc")
        'abcabcabc'
    """
    result = ""
    # Use a list to store temporary groups
    temp_groups = []
    
    # Check if the length of the string is a multiple of 3
    if len(s) % 3 == 0:
        # If it is, split the string into groups of 3
        groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range(len(s) // 3)]
    else:
        # If it is not, split the string into groups of 3 and add the remaining characters
        groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range(len(s) // 3)]
        
        # Add the remaining characters to the last group
        temp_groups.append(s[len(s) // 3 * 3:])
        
    # Cycle elements in each group
    for group in groups:
        if len(group) == 3:
            temp_groups.append(group[1:] + group[0])
    
    # Add any remaining groups to temp_groups
    if temp_groups:
        temp_groups += groups[-len(temp_groups):]
    
    # Remove any duplicate characters that were created when cycling groups
    result = "".join(["".join(i) for i in set(tuple(group) for group in temp_groups)])
    
    return result


# Test the functions
print(encode_cyclic("abcabcabc"))
print(decode_cyclic(encode_cyclic("abcabcabc")))
print(decode_cyclic("bcabcabcabc"))
```