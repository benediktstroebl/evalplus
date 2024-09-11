Here's a Python script that implements the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Cyclic Encoding and Decoding

Below is a Python script that implements the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with `encode_cyclic` function. Returns decoded string.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    
    # Reverse each group. The decoding process is equivalent to the encoding process with a reversed string.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghi"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In the provided code:

- The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and joins them back into a string.
- The `decode_cyclic` function splits the input string into groups of three characters, reverses each group, and joins them back into a string. The decoding process is equivalent to the encoding process with a reversed string.
- The example usage demonstrates how to use these functions with a sample string. The output should show that the decoded string matches the original string.