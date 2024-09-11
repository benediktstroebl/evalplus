### Cyclic Encoding and Decoding Script

Below is a Python script that includes the `encode_cyclic` and `decode_cyclic` functions to perform cyclic encoding and decoding operations on strings.

```markdown
### cyclic_encoding_decoding.py

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): Input string to be encoded.

    Returns:
    str: Encoded string.
    """
    # Split string into groups of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group if group length is 3
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
    # Initialize an empty string to store the decoded result
    decoded = ""
    
    # Initialize an index to track the current position in the string
    i = 0
    
    # Loop through the string until all characters have been processed
    while i < len(s):
        # Check if we are at the start of a new group
        if i % 3 == 0:
            # If so, extract the group and append it to the decoded string
            decoded += s[i:i+3]
            # Move the index 3 positions forward
            i += 3
        else:
            # If not, extract the remaining characters in the group and append them to the decoded string
            decoded += s[i:i+3][i%3:] + s[i:i+3][:i%3]
            # Move the index 3 positions forward
            i += 3
    
    return decoded


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = encode_cyclic(original_string)
    print(f"Original String: {original_string}")
    print(f"Cyclic Encoded String: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Cyclic Decoded String: {decoded_string}")
```

### Explanation:

*   The `encode_cyclic` function splits the input string into groups of 3 characters, cycles the elements in each group (unless the group has fewer than 3 characters), and returns the encoded string.
*   The `decode_cyclic` function takes the encoded string as input and restores the original string by identifying the start of each group, extracting the group, and cycling the elements in the group back to their original positions.
*   The example usage demonstrates how to encode and decode a string using these functions.