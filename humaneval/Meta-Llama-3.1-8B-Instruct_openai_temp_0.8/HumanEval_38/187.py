### Cyclic Encoding and Decoding
#### Problem Statement

Encode and decode a string by cycling groups of three characters.

#### Solution

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    :param s: the input string to be encoded
    :return: the encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: the input string encoded with encode_cyclic
    :return: the decoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group to its original order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
original_string = "abcdefg"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

This solution defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes an input string, splits it into groups of three characters, cycles the elements within each group, and returns the encoded string. The `decode_cyclic` function reverses the `encode_cyclic` process to obtain the original string. The example usage demonstrates how to use these functions to encode and decode a string.