Here's a self-contained Python script that implements the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Cyclic Encoder and Decoder
#### Using Python 3.8+

```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a string encoded with the encode_cyclic function.

    Args:
        s (str): The encoded string.

    Returns:
        str: The decoded string.
    """
    # Count the number of groups of 3 characters and the number of remaining characters
    num_groups = (len(s) + 2) // 3
    remaining_chars = len(s) % 3

    # Initialize a list to store the decoded groups
    decoded_groups = []

    # Loop over the groups and handle the remaining characters
    for i in range(num_groups):
        group_index = 3 * i
        # Extract the group of characters
        group = s[group_index:group_index + 3]
        # Cycle the characters in the group (if it has 3 characters)
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        else:
            # If the group has fewer than 3 characters, append it as is
            decoded_groups.append(group)

    # Handle the remaining characters
    if remaining_chars == 1:
        # If there's 1 remaining character, append it to the first group
        decoded_groups[0] = decoded_groups[0][:-1] + s[-1]
    elif remaining_chars == 2:
        # If there are 2 remaining characters, append them to the first group
        decoded_groups[0] = decoded_groups[0][:-2] + s[-2:] + decoded_groups[0][-1]

    # Join the decoded groups into a string
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcdefg"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This code provides the two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes an input string, splits it into groups of 3 characters, cycles the characters in each group (except for groups with fewer than 3 characters), and returns the encoded string. The `decode_cyclic` function takes an input string that was previously encoded using `encode_cyclic`, decodes it by cycling the characters in each group and handling any remaining characters at the end of the string, and returns the decoded string. The example usage demonstrates how to use these functions to encode and decode a string.