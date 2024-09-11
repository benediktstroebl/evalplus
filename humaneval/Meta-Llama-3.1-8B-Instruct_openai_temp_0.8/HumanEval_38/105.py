Here's the complete Python script that solves the problem:
```markdown
# Cyclic Encoding and Decoding Script

## encode_cyclic function
### Encodes a string by cycling groups of three characters.

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

## decode_cyclic function
### Decodes a string encoded with the encode_cyclic function.

```python
def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # reverse cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

## Example Usage
```python
# Example usage of the encode_cyclic and decode_cyclic functions
encoded_string = encode_cyclic("abcdef")
decoded_string = decode_cyclic(encoded_string)

print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
```

This script provides the `encode_cyclic` and `decode_cyclic` functions, which can be used to encode and decode strings by cycling groups of three characters. The example usage at the end demonstrates how to use these functions to encode and decode a string.