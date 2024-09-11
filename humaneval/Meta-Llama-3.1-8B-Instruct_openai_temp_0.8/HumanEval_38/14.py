```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefgh")
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In this script, we have the two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and then joins them together to form the encoded string. The `decode_cyclic` function does the opposite to reverse the encoding process.

The example usage demonstrates how to use these functions to encode and decode a string. In this case, the string "abcdefgh" is encoded and then decoded back to the original string.