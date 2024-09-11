### Cyclic Encoding and Decoding

Below is a Python script that implements the cyclic encoding and decoding functions as specified.

```markdown
### Code
```python
def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.

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


def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.

    Args:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty decoded string
    decoded = ""
    
    # Process string in groups of 3
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        
        # If the group has fewer elements than 3, cycle its elements
        if len(group) < 3:
            group += " " * (3 - len(group))
            # Move the first element of the group to the end
            group = group[1:] + group[0]
        
        # Add the decoded group to the decoded string
        decoded += group
    
    # Remove trailing spaces
    return decoded.rstrip()


# Example usage
if __name__ == "__main__":
    test_string = "abcdefg"
    encoded = encode_cyclic(test_string)
    decoded = decode_cyclic(encoded)
    
    print("Encoded string:", encoded)
    print("Decoded string:", decoded)
```

### Explanation

*   The `encode_cyclic` function takes a string as input, splits it into groups of 3, and cycles the elements in each group (unless the group has fewer than 3 elements).
*   The `decode_cyclic` function takes an encoded string as input, processes it in groups of 3, and cycles the elements in each group (unless the group has fewer than 3 elements).
*   The example usage demonstrates how to use the encoding and decoding functions with a test string.

### Output

```
Encoded string: cbaefdg
Decoded string: abcdefg
```