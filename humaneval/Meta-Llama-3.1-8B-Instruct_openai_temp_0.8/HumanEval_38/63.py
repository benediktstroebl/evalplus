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
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Initialize an empty string to store the decoded result.
    decoded_s = ""
    # Iterate over the encoded string in steps of 3.
    for i in range(0, len(s), 3):
        # Extract a group of 3 characters from the encoded string.
        group = s[i:i+3]
        # Check if the group has 3 characters.
        if len(group) == 3:
            # If the group has 3 characters, extract the first character and append the third character before the second character.
            decoded_s += group[2] + group[1] + group[0]
        else:
            # If the group has fewer characters, append the characters as is.
            decoded_s += group
    return decoded_s


# Test the functions
s = "abcdef"
encoded_s = encode_cyclic(s)
decoded_s = decode_cyclic(encoded_s)

print(f"Encoded string: {encoded_s}")
print(f"Decoded string: {decoded_s}")

assert s == decoded_s
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement a cyclic encoding and decoding algorithm for strings. The `encode_cyclic` function splits the input string into groups of 3 characters, cycles the elements in each group unless the group has fewer than 3 characters, and then joins the groups together. The `decode_cyclic` function takes the encoded string as input, iterates over the string in steps of 3, and extracts each group of 3 characters. If a group has 3 characters, it appends the third character before the second character; otherwise, it appends the characters as is. The script also includes a test case to verify that the encoding and decoding functions are correct.