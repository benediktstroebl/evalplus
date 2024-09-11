Here's the completed Python script:

```python
def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode groups by moving the first element to the end.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefghijklmnopqrstuvwxyz")
    decoded_str = decode_cyclic(encoded_str)
    
    print(f"Encoded string: {encoded_str}")
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions: `encode_cyclic` that encodes a given string by cycling groups of three characters, and `decode_cyclic` that decodes a string encoded using `encode_cyclic`. The example usage demonstrates how to use these functions to encode and decode a string.