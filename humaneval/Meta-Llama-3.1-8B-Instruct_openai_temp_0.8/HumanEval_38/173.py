### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to encode.
    :return: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Encoded string to decode.
    :return: Decoded string.
    """
    # Initialize result string
    decoded = ""
    index = 0
    
    # Loop through the string in steps of 3
    while index < len(s):
        # Get the group of 3, cycling elements if necessary
        group = s[index:min(index + 3, len(s))]
        
        # Rotate right by 1 if group has length 3
        if len(group) == 3:
            decoded += group[-1] + group[:-1]
        else:
            decoded += group
        
        index += 3
    
    return decoded


# Example usage:
if __name__ == "__main__":
    encoded = encode_cyclic("test123")
    print(f"Encoded: {encoded}")
    
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")
```

This script contains the `encode_cyclic` and `decode_cyclic` functions as specified in your task. It also includes an example usage section at the end, which demonstrates how to use these functions to encode and decode a test string.