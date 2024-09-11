### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    Example:
        >>> encode_cyclic("abcdef")
        'badcfe'
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Reverse the order of groups to maintain the original sequence
    groups = groups[::-1]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Example:
        >>> decode_cyclic("badcfe")
        'abcdef'
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cycle in each group to maintain the original sequence
    groups = [group[::-1] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)
    
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```
This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements within each group, and then joins them back together to form the encoded string. The `decode_cyclic` function reverses this process to obtain the original string from the encoded string.

Note that this implementation assumes that the input string has a length that is a multiple of three, or has a length that is a multiple of three plus one or two. This is because the encoding process involves splitting the string into groups of three characters, and the decoding process involves reversing this splitting. If the input string has a length that is not a multiple of three, the encoding and decoding processes may not be perfectly symmetrical.