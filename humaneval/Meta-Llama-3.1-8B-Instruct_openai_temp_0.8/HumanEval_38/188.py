### Cyclic Encoding and Decoding Script

The following script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and then cycles the elements in each group. The `decode_cyclic` function does the reverse operation to decode a string that has been encoded with `encode_cyclic` function.

```markdown
### Script
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Initialize result string
    decoded_string = ""
    # Initialize counter
    i = 0
    # Loop until all characters are processed
    while i < len(s):
        # If we have a group of three characters, cycle them
        if i + 2 < len(s):
            decoded_string += s[i + 2] + s[i + 1] + s[i]
        # If we don't have a group of three characters, just append the characters
        else:
            decoded_string += s[i:]
        i += 3
    return decoded_string


# Example usage
encoded_string = encode_cyclic("abcdef")
print("Encoded string:", encoded_string)

decoded_string = decode_cyclic(encoded_string)
print("Decoded string:", decoded_string)
```

This script first defines the `encode_cyclic` function, which cycles groups of three characters in a string. It then defines the `decode_cyclic` function, which does the reverse operation to decode a string that has been encoded with `encode_cyclic` function. The script finally demonstrates how to use these functions by encoding a string and then decoding it.