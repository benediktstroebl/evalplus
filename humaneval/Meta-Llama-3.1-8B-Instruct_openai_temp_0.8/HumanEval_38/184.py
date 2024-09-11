```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    :param s: string to be encoded
    :return: encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: string to be decoded
    :return: decoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # remove extra characters if any group has more than 3 characters
    groups = [group for group in groups if len(group) == 3]
    # reverse cycle in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script implements the `encode_cyclic` function to encode a string by cycling groups of three characters, and the `decode_cyclic` function to decode a string that was encoded with the `encode_cyclic` function. The script includes example usage to demonstrate the functionality of these functions. The decoded string is compared to the original string to verify the correctness of the decoding process.