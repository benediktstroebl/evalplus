### Cyclic Encoding and Decoding Script
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input encoded string
    :return: Decoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Check if all groups have exactly 3 characters
    if any(len(group)!= 3 for group in groups):
        raise ValueError("Invalid encoded string. It must be encoded with encode_cyclic function.")
    # Check if encoded string has any repeated groups
    if len(set(groups))!= len(groups):
        raise ValueError("Invalid encoded string. It must not have any repeated groups.")
    
    # Decode each group by shifting the first character to the end
    decoded_groups = [(group[-1] + group[:-1]) for group in groups]
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    original_string = "HelloWorld"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    try:
        decoded_string = decode_cyclic(encoded_string)
        print(f"Decoded string: {decoded_string}")
    except ValueError as e:
        print(f"Error: {e}")
```

This script defines `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string, decodes each group by shifting the first character to the end, and returns the decoded string. The example usage demonstrates how to use these functions.