### Cyclic Encoding and Decoding
#### Python Script

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.

    Args:
    s (str): input string to be encoded.

    Returns:
    str: encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # join groups to form encoded string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): encoded string to be decoded.

    Returns:
    str: decoded string.
    """
    # initialize decoded string
    decoded_str = ""
    # initialize temporary string to store current cycle
    cycle = ""
    # iterate over characters in encoded string
    for char in s:
        # add character to current cycle
        cycle += char
        # if cycle has 3 characters, add them to decoded string and reset cycle
        if len(cycle) == 3:
            # cycle elements in cycle (i.e., move first element to end)
            decoded_str += cycle[1:] + cycle[0]
            cycle = ""
    # if there are remaining characters in cycle, add them to decoded string
    if cycle:
        decoded_str += cycle
    return decoded_str


# example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("AttackatDawn")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In this code:

*   The `encode_cyclic` function splits the input string into groups of three characters and cycles the elements in each group, unless the group has fewer elements than three.
*   The `decode_cyclic` function iterates over the encoded string, adding characters to a temporary cycle string. When the cycle has three characters, it adds them to the decoded string and resets the cycle. Any remaining characters in the cycle are added to the decoded string at the end.
*   The example usage demonstrates how to use these functions to encode and decode a string.