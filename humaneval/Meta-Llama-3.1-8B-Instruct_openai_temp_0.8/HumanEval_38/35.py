```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    The encoding involves splitting the input string into groups of three characters.
    If a group has fewer than three characters, the last character is not repeated.
    The characters in each group are then rearranged to have the second character first,
    followed by the first character, and then the remaining characters (if any).
    
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
    
    The decoding involves splitting the input string back into groups of three characters.
    The characters in each group are then rearranged to have the first character first,
    followed by the second character, and then the remaining characters (if any).
    
    Args:
        s (str): The encoded string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Decode each group
    groups = [group[-1] + group[1:-1] + group[0] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
encoded_string = encode_cyclic("abcdefgh")
decoded_string = decode_cyclic(encoded_string)
print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

This script first defines the `encode_cyclic` function to encode a string by cycling groups of three characters. The `decode_cyclic` function then reverses this process to decode the string.

In the example usage, we first encode the string "abcdefgh" using the `encode_cyclic` function and store the result in `encoded_string`. We then decode `encoded_string` using the `decode_cyclic` function and store the result in `decoded_string`. Finally, we print out both the encoded and decoded strings to verify that the encoding and decoding process is correct.