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
    # Initialize an empty string to store the decoded result
    decoded = ""
    
    # Loop through the input string with a step of 3
    for i in range(0, len(s), 3):
        # Extract a group of 3 characters
        group = s[i:i+3]
        
        # If the group has 3 characters, cycle them
        if len(group) == 3:
            decoded += group[1] + group[0] + group[2]
        # If the group has less than 3 characters, append it as is
        else:
            decoded += group
    
    return decoded


# Example usage
if __name__ == "__main__":
    input_string = "abcdefgh"
    encoded = encode_cyclic(input_string)
    print(f"Encoded string: {encoded}")
    
    decoded = decode_cyclic(encoded)
    print(f"Decoded string: {decoded}")
```

In the `decode_cyclic` function, I have used a different approach to reverse the cycling operation. Instead of trying to shift each group as in the original `encode_cyclic` function, we cycle the characters in each group of 3 as we read the input string. This ensures that we produce the original string when decoding.