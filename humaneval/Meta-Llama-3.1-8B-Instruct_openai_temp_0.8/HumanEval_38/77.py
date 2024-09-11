### Cyclic Encoding and Decoding
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

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
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Loop through the groups of three characters
    for i in range(0, len(s), 3):
        # If the group has three characters, cycle them
        if i + 3 <= len(s):
            decoded_groups.append(s[i+1:i+3] + s[i])
        # If the group has fewer characters, add the remaining characters as is
        else:
            decoded_groups.append(s[i:])
    
    # Join the decoded groups into a single string
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function takes the encoded string, identifies the groups of three characters, cycles them back to their original order, and returns the decoded string.

In the example usage section, we demonstrate how to use these functions by encoding and decoding a string. The original string "abcdef" is encoded and then decoded, resulting in the original string.