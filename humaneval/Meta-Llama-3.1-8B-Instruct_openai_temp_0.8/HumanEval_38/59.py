```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with `encode_cyclic` function. Returns decoded string.
    """
    result = []
    while len(s) >= 3:
        # Extract last three characters, cycle them, and add to result
        group = s[-3:]
        result.append(group[1:] + group[0])
        # Remove the last three characters from the string
        s = s[:-3]
    # Add the remaining characters to the result
    result.append(s)
    return "".join(result[::-1])


# Example usage
original_string = "abcdef"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
```

The `decode_cyclic` function works by repeatedly extracting the last three characters from the encoded string, cycling them, and adding them to the result. This process is repeated until the string has fewer than three characters left, at which point the remaining characters are added to the result. The decoded string is then constructed by reversing the result.