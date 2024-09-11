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
    
    # cycle elements in each group to their original order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    # Test encode_cyclic function
    encoded = encode_cyclic("123456789")
    print(f"Encoded string: {encoded}")
    
    # Test decode_cyclic function
    decoded = decode_cyclic(encoded)
    print(f"Decoded string: {decoded}")
```
This script defines the `encode_cyclic` and `decode_cyclic` functions as specified. The `encode_cyclic` function takes a string, splits it into groups of three characters, and then cycles the elements within each group. The `decode_cyclic` function reverses the process by cycling the elements in each group back to their original order. The script also includes example usage in the `if __name__ == "__main__":` block to demonstrate how to use these functions.