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
    result = ""
    group_index = 0
    while group_index < len(s):
        group = s[group_index:group_index + 3]
        # if group is not complete, add missing characters
        if len(group) < 3:
            group = ('' if not group else group[0]) + ('' if group_index >= len(s) - 2 else s[group_index + 1]) + ('' if len(group) == 1 else group[1])
        # remove first character from the first position in group, and put it as the last one.
        result += group[-1] + group[:-1]
        group_index += 3
    return result


# Test the functions
s = "abcdef"
encoded_s = encode_cyclic(s)
print(f"Encoded '{s}': {encoded_s}")
decoded_s = decode_cyclic(encoded_s)
print(f"Decoded '{encoded_s}': {decoded_s}")
```

This script first defines the `encode_cyclic` function to encode a string by cycling groups of three characters. It then defines the `decode_cyclic` function to take an encoded string and decode it back to the original string. The `decode_cyclic` function works by iterating over the encoded string and removing the first character from each group and appending it to the end of the group, effectively reversing the grouping and cycling operation performed by `encode_cyclic`. Finally, the script tests the functions with a sample string.