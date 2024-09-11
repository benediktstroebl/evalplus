### Cyclic Encoding and Decoding Functionality

Below is a Python script that implements the `encode_cyclic` and `decode_cyclic` functions as described in the problem. The `decode_cyclic` function is completed for you.

```markdown
### cyclic_encoding.py
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
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script first defines the `encode_cyclic` and `decode_cyclic` functions as described. The `decode_cyclic` function works in a similar way to the `encode_cyclic` function but shifts the characters in the opposite direction. 

The example usage demonstrates how to use these functions by encoding and then decoding a sample string. The output should be the original string.