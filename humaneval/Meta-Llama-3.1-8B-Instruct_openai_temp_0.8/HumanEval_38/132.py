```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Split string to groups. Each of length 3, but with last group padded with spaces.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] + " " for i in range((len(s) + 2) // 3)]
    # Initialize result string.
    result = ""
    # Iterate over each group.
    for group in groups:
        # Remove padding spaces.
        if group[-2:] == " ":
            group = group[:-2]
        # If group is of length 2, first character moves to the end.
        if len(group) == 2:
            group = group[1] + group[0]
        # Add group to result string.
        result += group
    # Remove trailing space.
    return result.strip()


# Example usage
if __name__ == "__main__":
    original_string = "01234567890123456789"
    encoded_string = encode_cyclic(original_string)
    print("Encoded string:", encoded_string)
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
```

In this script, the `encode_cyclic` function encodes the input string by cycling groups of three characters. The `decode_cyclic` function takes the encoded string as input and decodes it back to its original form. The example usage at the end demonstrates how to use these functions.