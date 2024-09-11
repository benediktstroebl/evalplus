```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Parameters:
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
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdef")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In the `decode_cyclic` function, I've made a small modification to correctly cycle the elements in each group. The group is now cycled by appending the last character to the beginning of the group (`group[-1] + group[:-1]`). This is because the `encode_cyclic` function cycles the elements by shifting the characters one position to the right (`group[1:] + group[0]`).