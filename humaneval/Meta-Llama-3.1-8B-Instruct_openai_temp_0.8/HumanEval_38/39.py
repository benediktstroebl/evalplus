### Cyclic Encoding and Decoding

The following Python script implements cyclic encoding and decoding functions using the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # join all groups into a single string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by cycling elements to the beginning unless the group has fewer than 3 elements
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    # join all groups into a single string
    return "".join(groups)


# Example use case:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_cyclic` function, which splits the input string into groups of three characters and cycles the elements within each group to the beginning. The `decode_cyclic` function performs the reverse operation to decode the string.

The example use case demonstrates how to use these functions to encode and decode a string.