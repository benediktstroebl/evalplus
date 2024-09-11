### Cyclic Encoding and Decoding Script

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
    # split string to groups. Each of length 3
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group to original order
    groups = [(group[-1] + group[0:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# example usage
if __name__ == "__main__":
    encoded_string = encode_cyclic("abcdefgh")
    print(f"Encoded String: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions and includes an example usage in the `if __name__ == "__main__":` block.