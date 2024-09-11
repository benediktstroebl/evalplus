### Cyclic Encoding and Decoding Script

Here's a Python script that implements the `encode_cyclic` and `decode_cyclic` functions.

```markdown
### Code
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    The cycling of each group is done by moving the first character to the end, 
    effectively rotating the group by one position.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    # Pad the string with zeros to make its length a multiple of 3
    s = s.ljust(len(s) + len(s) % 3, '0')
    
    # split string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with `encode_cyclic` function. Returns decoded string.
    
    Args:
        s (str): Encoded string.

    Returns:
        str: Decoded string.
    """
    # split encoded string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # decode each group by moving the first character to the front, effectively rotating the group by one position
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # remove padding zeros from the decoded string
    return "".join(groups).rstrip('0')


# Example usage
if __name__ == "__main__":
    input_str = "abcdef"
    encoded_str = encode_cyclic(input_str)
    print(f"Encoded: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded: {decoded_str}")
```

### Explanation

The `encode_cyclic` function takes a string as input and encodes it by cycling groups of three characters. It first pads the string with zeros to make its length a multiple of 3. Then, it splits the string into groups of three characters and cycles each group by moving the first character to the end. The encoded string is then returned.

The `decode_cyclic` function takes an encoded string as input and decodes it. It first splits the encoded string into groups of three characters. Then, it decodes each group by moving the first character to the front, effectively rotating the group by one position. Finally, it removes any padding zeros from the decoded string and returns it.

The example usage demonstrates how to use these functions to encode and decode a string.