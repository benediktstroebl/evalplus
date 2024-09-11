### Encoding and Decoding Cyclic Strings
```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    The encoding process works as follows:
    - Split the input string into groups of three characters each.
    - Cycle the elements in each group, unless the group has fewer than three elements.
    - Join the grouped and cycled elements into a single string.

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


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    The decoding process works as follows:
    - Split the input string into groups of three characters each.
    - If a group has three characters, cycle them back to their original position.
    - Join the grouped and cycled elements into a single string.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[2] + group[1] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefgh")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script first defines the `encode_cyclic` function to encode a string by cycling groups of three characters. It then defines the `decode_cyclic` function to decode a string that was previously encoded by `encode_cyclic`. The example usage demonstrates how to use these functions to encode and then decode a string.