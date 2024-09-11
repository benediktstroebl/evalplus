## Cyclic Encoding and Decoding
Below is a Python script that implements the `encode_cyclic` and `decode_cyclic` functions.

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
    
    # Decode groups. This is equivalent to moving first element to the end of the group.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
input_str = "abcdefghi"
encoded_str = encode_cyclic(input_str)
decoded_str = decode_cyclic(encoded_str)

print(f"Input string: {input_str}")
print(f"Encoded string: {encoded_str}")
print(f"Decoded string: {decoded_str}")
```

This script provides the `encode_cyclic` function to encode the input string by cycling groups of three characters, and the `decode_cyclic` function to decode the string back to its original form. The `decode_cyclic` function essentially reverses the encoding process by moving the first element of each group to the end. The example usage demonstrates how to use these functions with a sample input string.