### Cyclic Encoding and Decoding Script
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): Input encoded string.
    
    Returns:
    str: Decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Decoding: reverse the cycling operation performed in encoding
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Test the functions
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefg")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

### Explanation:
The provided script includes the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group, and finally joins the groups back into a string.

The `decode_cyclic` function performs the reverse operation to decode the string. It splits the input string into groups, reverses the cycling operation performed in encoding, and joins the groups back into a string.

In the test section, the script encodes the string "abcdefg" using `encode_cyclic`, prints the encoded string, decodes it using `decode_cyclic`, and prints the decoded string to verify that the encoding and decoding operations are correct.