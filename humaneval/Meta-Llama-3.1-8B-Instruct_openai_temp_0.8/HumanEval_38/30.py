```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.

    Args:
    s (str): Input string.

    Returns:
    str: Encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): Input string.

    Returns:
    str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("HelloWorld")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which work together to implement a simple data encoding and decoding scheme where groups of three characters are cycled in the encoded string. The `decode_cyclic` function is slightly modified from the initial description to correctly implement the decoding process.