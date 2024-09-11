### Cyclic Encoding and Decoding
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
    decoded_groups = []
    group = ""
    for char in s:
        # append character to current group
        group += char
        # if group has 3 characters, cycle them and add to decoded groups
        if len(group) == 3:
            if len(group) == 3:
                decoded_groups.append(group[1:] + group[0])
            else:
                decoded_groups.append(group)
            # reset group to empty
            group = ""
    # if there are remaining characters in group, cycle them and add to decoded groups
    if group:
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        else:
            decoded_groups.append(group)
    return "".join(decoded_groups)


# Example usage:
original_string = "abcdef"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
```

The provided code includes the two functions, `encode_cyclic` and `decode_cyclic`, which implement the cyclic encoding and decoding logic. The example usage demonstrates how to encode and decode a string using these functions. The decoded string should be the same as the original string.