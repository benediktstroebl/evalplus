### Cyclic Encoding and Decoding in Python

This script implements cyclic encoding and decoding functions to manipulate strings.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): Input string to be decoded.

    Returns:
    str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. In reverse order to reverse the encoding.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
input_str = "Hello, World!"
encoded_str = encode_cyclic(input_str)
decoded_str = decode_cyclic(encoded_str)
print(f"Input: {input_str}")
print(f"Encoded: {encoded_str}")
print(f"Decoded: {decoded_str}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function takes the encoded string as input and returns the decoded string by reversing the encoding process.

The test code at the end demonstrates the usage of these functions by encoding a string, decoding the encoded string, and printing the results.