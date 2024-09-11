## Cyclic Encoding and Decoding
Here's the completed Python script that implements the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
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
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
        s (str): Encoded string to be decoded.
    
    Returns:
        str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by moving the first character to the end.
    # unless the group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
input_str = "abcdefgh"
encoded_str = encode_cyclic(input_str)
print(f"Encoded string: {encoded_str}")

decoded_str = decode_cyclic(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as described. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles the elements in each group (except for the last group which may have fewer elements), and returns the encoded string. The `decode_cyclic` function does the reverse: it splits the encoded string into groups, moves the first character of each group to the end (except for the last group), and returns the decoded string. The example usage demonstrates how to use these functions to encode and decode a test string.