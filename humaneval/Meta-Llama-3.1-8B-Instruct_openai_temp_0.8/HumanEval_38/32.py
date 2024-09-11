### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    # Split string into groups of 3 characters. Pad with spaces if necessary.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group, unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Remove any trailing spaces added during padding.
    groups = [group.rstrip() for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string to be decoded.
    :return: Decoded string.
    """
    # Split string into groups of 3 characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Find the index of the first group that has a non-space character in the second position
    # This is the index where the first group should be
    start_index = next(i for i, group in enumerate(groups) if'' not in group[1:])
    
    # If the index is 0, it means the second character of the first group should be at the end
    if start_index == 0:
        decoded_groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    else:
        decoded_groups = groups[:start_index]
        decoded_groups.extend([group[-1] + group[:-1] if len(group) == 3 else group for group in groups[start_index:]])
    
    return "".join(decoded_groups)


# Test the functions
if __name__ == "__main__":
    message = "hello world"
    encoded_message = encode_cyclic(message)
    print(f"Encoded message: {encoded_message}")
    
    decoded_message = decode_cyclic(encoded_message)
    print(f"Decoded message: {decoded_message}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified. The `encode_cyclic` function splits the input string into groups of 3 characters, cycles the elements in each group, and then joins them together. The `decode_cyclic` function splits the input string into groups of 3 characters, finds the index of the first group that should not be cycled, and then joins the groups together. The `if __name__ == "__main__":` block tests the functions with a sample message.