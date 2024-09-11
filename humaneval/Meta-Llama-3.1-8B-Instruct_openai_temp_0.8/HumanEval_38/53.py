```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    This function encodes a given string by splitting it into groups of 3, then cycles each group. 
    If a group has fewer than 3 characters, it is left unchanged.
    
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
    
    This function decodes a given string by splitting it into groups of 3, then rearranges each group. 
    If a group has fewer than 3 characters, it is left unchanged.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Rearrange elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
    return "".join(groups)

# Example usage:
if __name__ == "__main__":
    encoded = encode_cyclic("HelloWorld")
    print(f"Encoded: {encoded}")
    
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")
```

This script implements the `encode_cyclic` and `decode_cyclic` functions as described. The `encode_cyclic` function splits the input string into groups of 3, cycles each group (unless the group has fewer than 3 characters), and returns the encoded string. The `decode_cyclic` function reverses the process, rearranging each group to its original form and returning the decoded string.

The example usage at the end demonstrates how to use these functions to encode and decode a string.