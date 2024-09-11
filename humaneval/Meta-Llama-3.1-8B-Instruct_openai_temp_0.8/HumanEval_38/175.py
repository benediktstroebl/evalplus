### Cyclic Encoding and Decoding in Python

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
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by moving the first element to the end
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    test_string = "abcdefghi"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script implements both `encode_cyclic` and `decode_cyclic` functions as per the provided specifications. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group (unless the group has fewer than three elements), and returns the encoded string. The `decode_cyclic` function does the reverse, decoding the input string by moving the first element of each group to the end. The example usage demonstrates how to use these functions with a test string.