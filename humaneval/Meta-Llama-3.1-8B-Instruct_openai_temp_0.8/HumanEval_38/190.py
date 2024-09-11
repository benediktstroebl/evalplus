```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # decode groups by cycling elements and padding with last character
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            decoded_group = group[1:] + group[0]
        else:
            # if group has less than 3 elements, pad with last character
            last_char = groups[groups.index(group) + 1][0] if groups.index(group) + 1 < len(groups) else group[-1]
            decoded_group = group + last_char
        decoded_groups.append(decoded_group)
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    original_str = "abcdef"
    encoded_str = encode_cyclic(original_str)
    print("Original string:", original_str)
    print("Encoded string:", encoded_str)
    decoded_str = decode_cyclic(encoded_str)
    print("Decoded string:", decoded_str)
```

This script provides functions `encode_cyclic` and `decode_cyclic` as described in the problem. The `encode_cyclic` function takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string by cycling elements and padding with the last character of the adjacent group if necessary. The example usage demonstrates how to use these functions to encode and decode a string.