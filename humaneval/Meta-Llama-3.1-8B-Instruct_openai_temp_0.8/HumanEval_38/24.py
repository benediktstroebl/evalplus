### Cyclic Encoding and Decoding

Below is a Python script that includes the `encode_cyclic` and `decode_cyclic` functions to enable cyclic encoding and decoding of input strings.

```markdown
### cyclic_encoding_decoding.py

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Parameters:
    s (str): Input encoded string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # decode groups by cycling elements
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    input_string = "abcdefghi"
    encoded_string = encode_cyclic(input_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Explanation

This script includes:

1.  The `encode_cyclic` function, which splits the input string into groups of three characters. It then cycles the elements within each group, unless the group has fewer than three elements.
2.  The `decode_cyclic` function, which works in reverse by decoding the input string. It splits the string into groups of three characters and then cycles the elements within each group.
3.  Example usage that demonstrates how to use these functions to encode and decode a string.

The provided `decode_cyclic` function cycles the elements in each group in the opposite direction compared to the `encode_cyclic` function. This ensures that decoding the encoded string will result in the original input string.