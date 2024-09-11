### Cyclic Encoding and Decoding in Python

Here's a self-contained Python script that solves the cyclic encoding and decoding problem:

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split encoded string into groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # uniformize each group. We don't know the original order of elements.
    # So we just need to make sure the first element of the group (which was the second in the encoded string) is the first in the decoded string.
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
original_string = "abcdefgh"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print(f"Original: {original_string}")
print(f"Encoded: {encoded_string}")
print(f"Decoded: {decoded_string}")
```

This script will first encode a string using the `encode_cyclic` function, then decode the encoded string using the `decode_cyclic` function, and finally print the original, encoded, and decoded strings.