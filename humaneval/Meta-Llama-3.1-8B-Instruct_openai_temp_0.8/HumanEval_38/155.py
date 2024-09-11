### Cyclic Encoding and Decoding Script

Here's a Python script that implements the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Code

```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string to groups. Each of length 3
    groups = [
        s[(3 * i):min((3 * i + 3), len(s))] 
        for i in range((len(s) + 2) // 3)
    ]
    # Cycle elements in each group. Unless group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    :param s: Input encoded string
    :return: Decoded string
    """
    # Split string to groups. Each of length 3
    groups = [
        s[(3 * i):min((3 * i + 3), len(s))] 
        for i in range((len(s) + 2) // 3)
    ]
    # Reverse cycle in each group. Unless group has fewer elements than 3
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdef")
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

### Explanation

The `encode_cyclic` function works by splitting the input string into groups of three characters. If a group has fewer than three characters, it remains unchanged. The elements in each group are then cycled, with the first element moved to the end of the group.

The `decode_cyclic` function reverses the cycling process performed by `encode_cyclic`. It splits the input string into groups of three characters and then reverses the cycling operation by moving the last element to the front of each group.

The example usage demonstrates how to use these functions to encode and decode a string.