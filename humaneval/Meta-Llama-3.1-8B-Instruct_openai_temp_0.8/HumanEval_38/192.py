### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Groups with fewer than 3 characters are left unchanged.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Decoding is done by finding the previous encoding of the input string.
    This is a simple implementation, assuming no other char groups are used.
    """
    decoded = []
    encoded = ""

    # Find the original string (previous encoding of the decoded string)
    for group in encode_cyclic(s):
        if len(group) == 3:
            encoded += group[0] + group[1] + group[2]
        else:
            encoded += group

    # Split the encoded string back into groups of 3
    encoded_groups = [encoded[(3 * i):min((3 * i + 3), len(encoded))] for i in range((len(encoded) + 2) // 3)]

    # Reverse each group to find the original string
    decoded_groups = [(group[2] + group[1] + group[0]) if len(group) == 3 else group for group in encoded_groups]

    return "".join(decoded_groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script defines two functions `encode_cyclic` and `decode_cyclic` to perform cyclic encoding and decoding on strings. The `decode_cyclic` function assumes that the input string was encoded with `encode_cyclic` and does not account for any other possible encodings. The example usage demonstrates how to use these functions to encode and decode a string.