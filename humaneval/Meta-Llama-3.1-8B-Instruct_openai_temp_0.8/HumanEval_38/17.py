### Cyclic Encoding and Decoding in Python

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    :param s: Encoded string.
    :return: Decoded string.
    """
    # Initialize result string
    decoded_str = ""
    # Initialize index counter
    index = 0
    # Iterate over the input string.
    while index < len(s):
        # Get the current group size.
        group_size = 3 if index + 3 <= len(s) else len(s) - index
        # Get the current group
        group = s[index:index + group_size]
        # If group has fewer elements than 3, add them to the result string as is.
        if group_size < 3:
            decoded_str += group
        # Otherwise, cycle elements in the group.
        else:
            decoded_str += group[-1] + group[:-1]
        # Increment index counter
        index += group_size
    return decoded_str


# Example usage:
if __name__ == "__main__":
    original_str = "HelloWorld"
    encoded_str = encode_cyclic(original_str)
    print(f"Original String: {original_str}")
    print(f"Encoded String: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded String: {decoded_str}")
```

This script provides the `encode_cyclic` function that takes a string and cycles groups of three characters. The `decode_cyclic` function decodes the string that was encoded with the `encode_cyclic` function. The script includes example usage to demonstrate how to use these functions.