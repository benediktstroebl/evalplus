### Cyclic Encoding and Decoding in Python

Below is a self-contained Python script that provides both the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): Input string to be encoded.

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
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): Input encoded string.

    Returns:
        str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1:] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

In this script, the `encode_cyclic` function splits the input string into groups of three characters, then cycles the elements in each group. The `decode_cyclic` function reverses this process by reversing the cycle in each group. The `if __name__ == "__main__":` block provides an example usage of the functions with an original string, its encoded string, and the decoded string.