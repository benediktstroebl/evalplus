### Cyclic Encoding and Decoding

This script provides two functions: `encode_cyclic` and `decode_cyclic` for encoding and decoding a string by cycling groups of three characters.

```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over each character in the encoded string
    for char in s:
        # Add the character to the current group
        current_group += char
        # If the current group is 3 characters long or if it's the last character
        if len(current_group) == 3 or char == s[-1]:
            # If the current group is 2 characters long (the last group might be shorter)
            if len(current_group) == 2:
                # Double the first character of the group
                decoded_group = char * 2 + current_group[0]
            else:
                # If the group is 3 characters long, cycle it
                decoded_group = current_group[1:] + current_group[0]
            # Add the decoded group to the list
            decoded_groups.append(decoded_group)
            # Reset the current group
            current_group = ""
    
    # Join the decoded groups into a single string and return it
    return "".join(decoded_groups)


# Example usage
encoded_string = encode_cyclic("hello world")
print(f"Encoded string: {encoded_string}")
decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```
This script first defines the `encode_cyclic` function, which takes a string `s` as input, splits it into groups of 3 characters (or less if the string length is not a multiple of 3), cycles the characters within each group (unless the group has fewer than 3 characters), and returns the encoded string.

The `decode_cyclic` function takes an encoded string as input, iterates over its characters, and constructs the decoded groups by cycling the characters within each group (or doubling the first character if the group has only 2 characters). Finally, it returns the decoded string.

The example usage demonstrates how to use these functions to encode and decode a string.