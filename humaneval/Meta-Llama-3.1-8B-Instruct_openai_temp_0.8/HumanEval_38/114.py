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
    # reverse encoding by shifting elements back in groups of three
    groups = []
    group_index = 0
    i = 0
    while i < len(s):
        if len(groups) == group_index:
            groups.append("")
        # add zero to end of group until it has 3 elements.
        while len(groups[group_index]) < 3:
            groups[group_index] += s[i]
            i += 1
        # shift right if group has 3 elements.
        if len(groups[group_index]) == 3:
            groups[group_index] = groups[group_index][1:] + groups[group_index][0]
        group_index += 1
    # combine groups into string
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    s = "abcdef"
    encoded = encode_cyclic(s)
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")
```

In this code, `encode_cyclic` function takes an input string and splits it into groups of three characters, cycling the first element in each group to the end of the group. The `decode_cyclic` function does the reverse, shifting the elements back in each group and combining them into the original string. The example usage at the end demonstrates how to use these functions.