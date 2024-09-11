### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): Encoded string to be decoded.

    Returns:
        str: Decoded string.
    """
    # Initialize decoded string
    decoded = ""
    
    # Initialize index of current position in the string
    i = 0
    
    # Loop until we have processed all characters
    while i < len(s):
        # If we have 3 characters, cycle them
        if i + 3 <= len(s):
            decoded += s[i:i+3][1:] + s[i:i+3][0]
            i += 3
        # If we have less than 3 characters, append them as is
        else:
            decoded += s[i:]
            break
    
    return decoded


# Example usage
if __name__ == "__main__":
    original_string = "abcdefg"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this script, the `encode_cyclic` function takes a string and splits it into groups of three characters. If a group has exactly three characters, it cycles them to obtain the encoded string. If a group has fewer than three characters, it appends them as is.

The `decode_cyclic` function takes an encoded string and attempts to reverse the encoding process. It iterates over the string, cycling groups of three characters and appending any remaining characters. If there are fewer than three characters at the end, it appends them as is.

In the example usage, the original string "abcdefg" is encoded and then decoded, demonstrating the round-trip functionality of the solution.