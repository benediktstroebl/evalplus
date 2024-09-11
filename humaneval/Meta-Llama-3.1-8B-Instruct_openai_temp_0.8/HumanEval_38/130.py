### Cyclic Encoding and Decoding

The following Python script provides functions for encoding and decoding a string in a cyclic manner.

```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.
    
    Args:
        s (str): Input string to be encoded.
    
    Returns:
        str: Encoded string with cyclic groups.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a string that was encoded with encode_cyclic function.
    
    Args:
        s (str): Input string to be decoded.
    
    Returns:
        str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse cycling in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("123456789")
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines the `encode_cyclic` function to encode a string by cycling groups of three characters, and the `decode_cyclic` function to reverse this process. The example usage demonstrates how to use these functions to encode and decode a string.