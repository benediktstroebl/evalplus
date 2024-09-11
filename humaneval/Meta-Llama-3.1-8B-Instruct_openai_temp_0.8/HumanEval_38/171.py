### Cyclic Encoding and Decoding

The following Python script implements the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.

    Args:
    s (str): The input string to encode.

    Returns:
    str: The encoded string.
    """
    # Split the string into groups of three characters.
    # We use the `min` function to prevent an `IndexError` for strings with less than three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Cycle the elements in each group unless the group has fewer elements than three.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]

    # Join the groups into a single string and return it.
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a string encoded with the `encode_cyclic` function.

    Args:
    s (str): The encoded string to decode.

    Returns:
    str: The decoded string.
    """
    # Split the encoded string into groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Initialize an empty list to store the decoded groups.
    decoded_groups = []

    # Iterate over the groups.
    for group in groups:
        # If the group has three characters, cycle them back to their original position.
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        # If the group has fewer than three characters, append it to the decoded groups as is.
        else:
            decoded_groups.append(group)

    # Join the decoded groups into a single string and return it.
    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script defines the `encode_cyclic` function to encode a string by cycling groups of three characters and the `decode_cyclic` function to decode a string encoded with `encode_cyclic`. The example usage demonstrates how to use these functions with a sample string.