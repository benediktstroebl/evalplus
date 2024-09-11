### Cyclic Encoding and Decoding
#### Problem Statement
Implement a function to encode a string by cycling groups of three characters and a function to decode the string.

#### Solution
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
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store the decoded groups
    decoded_groups = []
    # Initialize an index to keep track of the current position in the string
    i = 0
    # Loop until we've processed the entire string
    while i < len(s):
        # If we have at least 3 characters left in the string, create a group of 3
        if i + 3 <= len(s):
            group = s[i:i+3]
        # Otherwise, create a group of the remaining characters
        else:
            group = s[i:]
        # If the group has only 1 character, add it to the decoded groups as is
        if len(group) == 1:
            decoded_groups.append(group)
        # If the group has only 2 characters, add them to the decoded groups in the correct order
        elif len(group) == 2:
            decoded_groups.append(group[1] + group[0])
        # If the group has 3 characters, add them to the decoded groups in the correct order
        else:
            decoded_groups.append(group[1:] + group[0])
        # Move on to the next position in the string
        i += 3
    # Join the decoded groups into a single string and return it
    return "".join(decoded_groups)


# Example usage:
encoded_str = encode_cyclic("HelloWorld")
decoded_str = decode_cyclic(encoded_str)
print("Encoded string:", encoded_str)
print("Decoded string:", decoded_str)
```
This solution works by first splitting the input string into groups of 3 characters. The `encode_cyclic` function then cycles the elements in each group, unless the group has fewer than 3 characters. The `decode_cyclic` function works by looping through the string, creating groups of 3 characters, and cycling the elements in each group to recover the original string.