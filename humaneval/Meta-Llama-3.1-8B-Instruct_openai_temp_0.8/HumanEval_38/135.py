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
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group back to their original position. 
    # Unless group has fewer elements than 3.
    groups = [(len(group) == 3 and group[-1] + group[1:] or group) for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefgh")
    print(f"Encoded String: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded String: {decoded_str}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, to encode and decode a string by cycling groups of three characters. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function reverses this process to decode the string. The example usage at the end demonstrates how to use these functions.