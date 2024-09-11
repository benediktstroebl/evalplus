```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
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
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Split string to groups
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Decode each group by moving first element to the end unless group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    # Original string
    original_string = "abcdefghij"
    
    # Encode the string
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    # Decode the string
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

The provided script defines two functions, `encode_cyclic` and `decode_cyclic`, for encoding and decoding strings using the cyclic rotation of groups of three characters. The encoding process works by splitting the input string into groups of three characters, cycling the elements in each group (unless the group has fewer elements than three), and then joining the groups back together. The decoding process reverses the encoding process by cycling the elements in each group in the opposite direction. The example usage demonstrates the encoding and decoding of a sample string.