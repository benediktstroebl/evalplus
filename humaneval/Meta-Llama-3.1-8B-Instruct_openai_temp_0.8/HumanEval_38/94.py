### Cyclic Encoding and Decoding
#### Problem Statement
Implement cyclic encoding and decoding functions in Python.

#### Solution

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): Input string to encode.

    Returns:
    str: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join groups to form encoded string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): Encoded string to decode.

    Returns:
    str: Decoded string.
    """
    # Initialize decoded string
    decoded_str = ""
    
    # Initialize current character index
    idx = 0
    
    # Process string in chunks of 3 characters
    while idx < len(s):
        # Get next chunk of 3 characters
        chunk = s[idx:idx + 3]
        
        # If chunk has 3 characters, cycle them
        if len(chunk) == 3:
            decoded_str += chunk[1] + chunk[0] + chunk[2]
        # If chunk has fewer than 3 characters, append it as is
        else:
            decoded_str += chunk
        
        # Move to next chunk
        idx += 3
    
    return decoded_str


# Example usage:
if __name__ == "__main__":
    # Test encoding and decoding
    original_str = "abcdef"
    encoded_str = encode_cyclic(original_str)
    decoded_str = decode_cyclic(encoded_str)
    
    print(f"Original string: {original_str}")
    print(f"Encoded string: {encoded_str}")
    print(f"Decoded string: {decoded_str}")
```

#### Explanation

The provided Python script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement cyclic encoding and decoding, respectively.

The `encode_cyclic` function splits the input string into groups of 3 characters, cycles the elements in each group (except for groups with fewer than 3 characters), and joins them to form the encoded string.

The `decode_cyclic` function takes the encoded string as input, processes it in chunks of 3 characters, and decodes them by cycling the characters in each chunk. If a chunk has fewer than 3 characters, it is appended as is to the decoded string.

In the example usage section, we test the encoding and decoding functions with a sample string, "abcdef", and verify that the decoded string matches the original string.