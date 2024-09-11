### Cyclic Encoding and Decoding

Here's a self-contained Python script that completes the implementation of the `encode_cyclic` and `decode_cyclic` functions to solve the problem.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse cycle in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    # Test the encode and decode functions
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function rearranges the characters of the input string into groups of three, cycling the characters within each group unless the group has fewer than three characters. The `decode_cyclic` function does the reverse operation to recover the original string from the encoded string.

The example usage demonstrates how to use these functions to encode and decode a string, and prints the results to the console.