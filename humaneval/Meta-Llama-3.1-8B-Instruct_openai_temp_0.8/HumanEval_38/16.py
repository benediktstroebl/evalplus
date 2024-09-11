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
    decoded_groups = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        # decode group. If group has fewer elements than 3, just add it as is.
        if len(group) == 3:  # if group has 3 elements, cycle them.
            decoded_groups.append(group[1:] + group[0])
        else:  # if group has fewer elements, add it as is.
            decoded_groups.append(group)

    # join all decoded groups to one string.
    return "".join(decoded_groups)


# example usage:
s = "abcdefgh"
encoded = encode_cyclic(s)
print(f"Cyclic encoded string: {encoded}")
decoded = decode_cyclic(encoded)
print(f"Decoded string: {decoded}")
```

In this script, the `encode_cyclic` function takes a string `s` and splits it into groups of three characters each. It then cycles the elements in each group, unless the group has fewer elements than three. The decoded string is then returned.

The `decode_cyclic` function takes an encoded string and splits it into groups of three characters each. If a group has exactly three elements, it is decoded by cycling the elements. Otherwise, the group is added as is. The decoded groups are then joined together to form the decoded string.