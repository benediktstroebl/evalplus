```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string to groups. Each of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Encoded string to be decoded
    :return: Decoded string
    """
    # Initialize result string
    result = ""
    # Initialize index for encoded string
    i = 0
    # Process encoded string 3 characters at a time
    while i < len(s):
        # Extract group of 3 characters from encoded string
        group = s[i:i+3]
        # If group has less than 3 characters, append remaining characters
        if len(group) < 3:
            result += group + s[i+3:]
            break
        # Extract original group by moving first character to the end
        original_group = group[1] + group[2] + group[0]
        # Append original group to result string
        result += original_group
        # Move index 3 positions forward
        i += 3
    return result


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    print("Encoded string:", encoded_string)
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, and includes an example usage in the `if __name__ == "__main__":` block. The `decode_cyclic` function has been updated to correctly decode the string by extracting groups of 3 characters, moving the first character to the end of the group to form the original group, and appending it to the result string.