### Cyclic Encoding and Decoding
#### Python Script

```python
def encode_cyclic(s: str):
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


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Encoded string
    :return: Decoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Decode each group by moving first character to end, unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    input_str = "abcdefg"
    encoded_str = encode_cyclic(input_str)
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This Python script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string by reversing the encoding process.

In the example usage section, we demonstrate the usage of these functions by encoding a string "abcdefg" and then decoding the resulting encoded string.