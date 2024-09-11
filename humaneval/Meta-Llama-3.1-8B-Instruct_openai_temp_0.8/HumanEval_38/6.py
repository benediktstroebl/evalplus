```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    The function splits the input string into groups of three characters. 
    If a group has fewer than three characters, it remains unchanged. 
    Then the function cycles the elements of each group by moving the first element to the end, 
    unless it has fewer than three characters.
    
    Parameters:
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
    
    The function splits the input string into groups of three characters, 
    cycles the elements of each group (if necessary), and then concatenates the groups.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Initialize an empty string to store the decoded string
    decoded_string = ""
    # Initialize an empty string to store the current group
    group = ""
    # Iterate over each character in the input string
    for char in s:
        # Add the character to the current group
        group += char
        # If the current group has three characters, cycle them and add the decoded characters to the decoded string
        if len(group) == 3:
            decoded_string += group[1] + group[0] + group[2]
            # Reset the current group
            group = ""
    # If the current group has fewer than three characters, add the decoded characters to the decoded string
    if group:
        decoded_string += group
    return decoded_string


# Example usage:
s = "abcde"
encoded_string = encode_cyclic(s)
print("Encoded string:", encoded_string)
decoded_string = decode_cyclic(encoded_string)
print("Decoded string:", decoded_string)
```

This Python script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and then cycles the elements of each group (if necessary) to produce the encoded string. The `decode_cyclic` function takes the encoded string as input, splits it into groups of three characters, cycles the elements of each group (if necessary), and then concatenates the groups to produce the decoded string. The script also includes an example usage of these functions.