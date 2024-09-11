### Cyclic Encoding and Decoding in Python
#### Introduction
This script provides functions for encoding and decoding strings using a cyclic pattern. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function reverses the process to obtain the original string.

#### Code

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
    # decode cyclic string by taking each group, and taking the first element of the group.
    decoded_groups = [group[0] + group[1:] if len(group) == 3 else group for group in [s[i:i+3] for i in range(0, len(s), 3)]]
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    # encode a string
    original_string = "hello world"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    # decode the encoded string
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Explanation
1.  The `encode_cyclic` function splits the input string into groups of three characters. If the length of the string is not a multiple of three, it appends empty strings to the list of groups to make their length a multiple of three.
2.  For each group of three characters, it cycles the elements by moving the first character to the end of the group.
3.  The `decode_cyclic` function splits the encoded string into groups of three characters and then moves the first character of each group to the front to obtain the original string.
4.  The example usage demonstrates how to use these functions to encode and decode a string.