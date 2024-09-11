### Cyclic Encoding and Decoding Script

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
    # split encoded string to groups
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group back to its original position
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            decoded_group = group[1:] + group[0]
        else:
            decoded_group = group
        decoded_groups.append(decoded_group)
    # join groups back into a single string
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string by cycling the elements in each group back to their original position.

In the example usage section, we demonstrate how to use these functions by encoding and then decoding a test string.