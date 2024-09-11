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
    # Initialize an empty string to store the decoded result
    decoded_s = ""
    
    # Initialize an empty string to store the current group
    group = ""
    
    # Iterate over each character in the encoded string
    for char in s:
        # Add the character to the current group
        group += char
        
        # If the current group has 3 characters, decode it and add it to the decoded string
        if len(group) == 3:
            decoded_s += group[1:] + group[0]
            group = ""
    
    # If there are remaining characters in the current group, decode them and add them to the decoded string
    if group:
        decoded_s += group
    
    return decoded_s


# Example usage:
encoded_str = encode_cyclic("HelloWorld")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function encodes a given string by cycling groups of three characters. The `decode_cyclic` function decodes a string that was previously encoded using the `encode_cyclic` function. The script also includes an example usage of the two functions to demonstrate how they work.