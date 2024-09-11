```markdown
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
    # Reverse cycling in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefghijklmnopqrstuvwxyz")
    print("Encoded string:", encoded_str)

    decoded_str = decode_cyclic(encoded_str)
    print("Decoded string:", decoded_str)
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement the cyclic encoding and decoding functionalities as per the provided specifications. The `encode_cyclic` function splits the input string into groups of three characters and cycles them in each group. The `decode_cyclic` function reverses this process to decode the string. The example usage demonstrates the functionality of these functions.