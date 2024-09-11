### Cyclic Encoding and Decoding

Here's the Python script that implements the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Code

```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.
    
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


def decode_cyclic(s: str):
    """
    Decodes a string encoded with the `encode_cyclic` function.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    decoded_string = ""
    index = 0
    while index < len(s):
        # find the next group of 3 characters
        end_index = min(index + 3, len(s))
        group = s[index:end_index]
        # decode the group by shifting the first character to the front
        decoded_string += group[-1] + group[:-1]
        index = end_index
    return decoded_string


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("HelloWorld")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

### Explanation

The `encode_cyclic` function splits the input string into groups of three characters. If a group has fewer than three characters, it remains unchanged. Each group is then cycled by moving the first character to the end.

The `decode_cyclic` function takes an encoded string as input. It iterates through the string, decoding each group of three characters by shifting the first character to the front.

In the example usage, we encode the string "HelloWorld" using `encode_cyclic` and print the encoded string. We then decode the encoded string using `decode_cyclic` and print the decoded string, which should match the original input string.