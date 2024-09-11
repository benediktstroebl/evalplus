### Cyclic Encoding and Decoding in Python
#### Problem Description

The following Python script solves the problem of cyclic encoding and decoding. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes a string encoded with `encode_cyclic` as input and returns the decoded string.

#### Code
```markdown
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
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by cycling elements back to their original position.
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        else:
            decoded_groups.append(group)
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdef")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

#### Explanation

The `encode_cyclic` function works by splitting the input string into groups of three characters. If a group has fewer than three characters, it is left unchanged. Otherwise, the elements in the group are cycled by moving the first element to the end of the group.

The `decode_cyclic` function works by reversing the operation performed by `encode_cyclic`. It splits the input string into groups of three characters, just like `encode_cyclic`. However, each group is decoded by cycling the elements back to their original position. If a group has fewer than three characters, it is left unchanged.

In the example usage, we demonstrate how to use the `encode_cyclic` and `decode_cyclic` functions to encode and decode a string.