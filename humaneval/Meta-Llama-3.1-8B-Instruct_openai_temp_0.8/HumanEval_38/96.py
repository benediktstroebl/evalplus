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
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # decode each group back to the original order
    for group in groups:
        # cycle elements in each group. Unless group has fewer elements than 3.
        if len(group) == 3:
            result += group[2] + group[1] + group[0]
        elif len(group) == 2:
            result += group[1] + group[0]
        else:
            result += group

    return result


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefghij")
    print("Encoded string:", encoded_str)

    decoded_str = decode_cyclic(encoded_str)
    print("Decoded string:", decoded_str)
```

This script includes both the `encode_cyclic` and `decode_cyclic` functions to encode and decode the string using cyclic groups of characters. The `decode_cyclic` function reverses the process of `encode_cyclic` to obtain the original string.