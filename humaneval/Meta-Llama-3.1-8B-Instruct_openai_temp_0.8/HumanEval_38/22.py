## Cyclic Encoding and Decoding
### Problem Description
The following Python script provides implementations for cyclic encoding and decoding. 

### Code
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "HelloWorld"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Explanation
This script defines two functions: `encode_cyclic` and `decode_cyclic`. 

1.  The `encode_cyclic` function takes an input string `s`, splits it into groups of three characters, cycles the elements in each group (unless the group has fewer than three elements), and returns the encoded string.
2.  The `decode_cyclic` function takes an input string `s`, splits it into groups of three characters, reverses the cycle in each group (unless the group has fewer than three elements), and returns the decoded string.
3.  In the example usage section, we demonstrate how to use these functions by encoding and decoding the string "HelloWorld".