### Cyclic Encoding and Decoding

```python
def encode_cyclic(s: str):
    """
    Encodes the input string by cycling groups of three characters.

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


def decode_cyclic(s: str):
    """
    Decodes the input string encoded with encode_cyclic function.

    Args:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group back to original order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    test_string = "abcdefgh"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement the cyclic encoding and decoding algorithms. The `encode_cyclic` function takes an input string and splits it into groups of three characters. It then cycles the elements in each group, unless the group has fewer than three elements. The `decode_cyclic` function reverses the encoding process by cycling the elements in each group back to their original order.

The example usage demonstrates how to use these functions. It first encodes a test string, and then decodes the encoded string to recover the original string.