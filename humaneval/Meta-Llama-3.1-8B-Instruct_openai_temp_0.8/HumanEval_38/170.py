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
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Decode each group by moving the first character to the end. Unless group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefg")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In the above code, the `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements within each group (unless the group has fewer than three characters), and returns the encoded string. The `decode_cyclic` function does the reverse operation to decode the string. The example usage demonstrates how to use these functions to encode and decode a string.