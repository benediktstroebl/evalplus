### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Encoded string
    :return: Decoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse cycle in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which perform cyclic encoding and decoding, respectively. The `encode_cyclic` function splits the input string into groups of three characters and then cycles the elements in each group. The `decode_cyclic` function reverses this process by cycling the elements in each group in the opposite direction.

The script includes a test at the end that demonstrates how to use these functions by encoding and decoding the string "Hello, World!".