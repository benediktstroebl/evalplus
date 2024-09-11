### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded
    :return: Cyclically encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string to be decoded
    :return: Decoded string
    """
    # Split encoded string to groups
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    
    # Decode each group by moving the first character to the end
    decoded_groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    
    return "".join(decoded_groups)


# Example usage:
input_string = "abcdefghi"
encoded_string = encode_cyclic(input_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string, splits it into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string, splits it into groups, and reverses the cycle operation to retrieve the original string.

The example usage at the end demonstrates how to use these functions to encode and decode a string.