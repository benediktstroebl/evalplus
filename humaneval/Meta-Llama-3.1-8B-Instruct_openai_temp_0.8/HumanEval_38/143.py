### Cyclic Encoding and Decoding Script
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
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
    s (str): Input encoded string.

    Returns:
    str: Decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Decode each group by moving first element to the end. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    original_string = "123456789012"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script defines the `encode_cyclic` function to encode a given string by cycling groups of three characters and the `decode_cyclic` function to decode the encoded string. The example usage demonstrates how to use these functions to encode and decode a test string.