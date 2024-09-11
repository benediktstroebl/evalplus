### Cyclic Encoding and Decoding in Python

Below is a Python script that includes both the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    The encoding process works as follows:
    - Split the string into groups of three characters.
    - For each group with three characters, cycle them (i.e., move the first character to the end).
    - If a group has fewer than three characters, leave it as is.
    
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
    
    The decoding process works as follows:
    - Split the string into groups of three characters.
    - For each group with three characters, cycle them back to their original order.
    - If a group has fewer than three characters, leave it as is.
    
    :param s: the encoded string to be decoded
    :return: the decoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group back to their original order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
message = "abcdefg"
encoded = encode_cyclic(message)
decoded = decode_cyclic(encoded)

print(f"Encoded message: {encoded}")
print(f"Decoded message: {decoded}")
```

When you run the script, it will encode the string `"abcdefg"` using `encode_cyclic`, then decode the result using `decode_cyclic`, and print the encoded and decoded messages.