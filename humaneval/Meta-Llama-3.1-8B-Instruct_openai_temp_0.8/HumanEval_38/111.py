```markdown
### Cyclic Encoding and Decoding Script

This script provides functions for encoding and decoding strings using a cyclic pattern.
The `encode_cyclic` function takes a string and splits it into groups of three characters each,
then cycles the elements in each group. The `decode_cyclic` function reverses this process.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
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
    Takes as input string encoded with `encode_cyclic` function. Returns decoded string.
    
    Args:
    s (str): Input encoded string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse cycle elements in each group.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("1234567890")
    print(f"Encoded String: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded String: {decoded_str}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function reverses this process by cycling the elements in each group in the reverse direction.

In the example usage section, we demonstrate the usage of these functions by encoding a string and then decoding it back to the original string.