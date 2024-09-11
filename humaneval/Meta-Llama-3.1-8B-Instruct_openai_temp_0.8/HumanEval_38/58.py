```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
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
        s (str): The encoded string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # decode groups by concatenating each group with its own first character.
    decoded_groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)


# Example use case
if __name__ == "__main__":
    encode = encode_cyclic
    decode = decode_cyclic
    original_string = "abcdefg"
    encoded_string = encode(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

The `decode_cyclic` function splits the input string into groups of three characters and then decodes each group by moving the first character to the end of the group. If a group has fewer than three characters, it is left unchanged. The decoded groups are then joined together to form the final decoded string.

This script includes example use cases for both `encode_cyclic` and `decode_cyclic` functions. It encodes a string using `encode_cyclic`, prints the encoded string, decodes the string using `decode_cyclic`, and prints the decoded string.