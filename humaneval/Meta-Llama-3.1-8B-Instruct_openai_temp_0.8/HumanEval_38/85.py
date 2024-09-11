### Cyclic Encoding and Decoding
Below is a Python script that includes the `encode_cyclic` and `decode_cyclic` functions.

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
    
    # Decode groups by shifting the first element to the end of the group.
    # Unless the group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghij"
    encoded_string = encode_cyclic(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified and includes an example usage in the `if __name__ == "__main__":` block. The `encode_cyclic` function cycles the elements in each group of three characters, and the `decode_cyclic` function reverses this process.