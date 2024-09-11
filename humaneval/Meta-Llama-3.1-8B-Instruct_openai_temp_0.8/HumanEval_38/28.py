```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    :param s: input string
    :return: encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: encoded string
    :return: decoded string
    """
    # Initialize an empty string to store the decoded result
    decoded_str = ""
    
    # Initialize an empty string to store the current group
    group = ""
    
    # Iterate over the input string
    for char in s:
        # Remove the current character from the group
        group = group[1:] if group else group
        
        # Add the removed character to the decoded string
        decoded_str += char
        
        # Add the current character to the group
        group += char
        
        # If the group has 3 characters, reset it
        if len(group) == 3:
            group = ""
    
    # If the input string is not a multiple of 3, the group will still have characters
    if group:
        # Cycle the characters in the group
        decoded_str += group[1:] + group[0]
    
    return decoded_str


# Example usage:
encoded_str = encode_cyclic("HelloWorld")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

In this code, the `encode_cyclic` function splits the input string into groups of three characters, cycles the characters in each group, and returns the encoded string. The `decode_cyclic` function takes the encoded string as input, restores the original groups, and returns the decoded string.