### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string
    :return: Encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string
    :return: Decoded string
    """
    # Split string to groups of length 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)
    
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```
This script defines two functions, `encode_cyclic` and `decode_cyclic`, for cyclic encoding and decoding of strings. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements within each group (unless the group has fewer than three elements), and returns the encoded string. The `decode_cyclic` function reverses the process by splitting the encoded string into groups of three characters and cycling the elements in each group in the opposite direction. The script includes an example usage at the end to demonstrate the functionality of the two functions.