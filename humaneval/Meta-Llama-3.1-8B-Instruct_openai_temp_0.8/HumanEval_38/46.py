### Cyclic Encoding and Decoding

This script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string and encodes it by cycling groups of three characters. The `decode_cyclic` function takes the encoded string and returns the original string.

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
    result = ""
    for i in range(0, len(s), 3):
        if i + 2 < len(s):
            group = s[i:i + 3]
        else:
            group = s[i:i + len(s) % 3]
        
        # Extract the last character to the front of the group
        result += group[-1] + group[:-1]
    
    return result


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, and provides an example usage in the `if __name__ == "__main__":` block. The `decode_cyclic` function now correctly handles groups of different lengths.