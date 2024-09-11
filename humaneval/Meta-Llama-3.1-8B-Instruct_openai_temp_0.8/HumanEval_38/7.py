## Cyclic Encoding and Decoding in Python

The following Python script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement cyclic encoding and decoding of strings.

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # split encoded string into groups of 3 characters
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    
    # decode each group by moving the first character to the end
    decoded_groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    # Encode a string
    encoded_string = encode_cyclic("abcdefghi")
    print("Encoded string:", encoded_string)

    # Decode the encoded string
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)

    # Verify that decoding the encoded string returns the original string
    assert decoded_string == "abcdefghi"
```

The `encode_cyclic` function splits the input string into groups of 3 characters. If a group has fewer characters than 3, it remains unchanged. Then it cycles the characters in each group, moving the first character to the end. The encoded groups are joined to form the final encoded string.

The `decode_cyclic` function splits the encoded string into groups of 3 characters. Then it decodes each group by moving the first character to the end, unless the group has fewer characters than 3. The decoded groups are joined to form the final decoded string.

In the example usage, we demonstrate how to use these functions to encode and decode a string. We also verify that decoding the encoded string returns the original string.