```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded.
    :return: Encoded string with cyclic groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string to be decoded.
    :return: Decoded string.
    """
    # split encoded string into groups
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # decode each group
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # if group has three characters, move the last character to the beginning and join the rest
            decoded_groups.append(group[-1] + group[:-1])
        else:
            # if group has less than three characters, add the group as it is
            decoded_groups.append(group)
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("HelloWorld")
    print("Encoded string:", encoded_str)
    decoded_str = decode_cyclic(encoded_str)
    print("Decoded string:", decoded_str)
```

This script provides both the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and cyclically shifts the characters within each group. The `decode_cyclic` function reverses this process by shifting the characters back and reassembling the original string. The `if __name__ == "__main__":` block demonstrates how to use these functions with the string "HelloWorld".