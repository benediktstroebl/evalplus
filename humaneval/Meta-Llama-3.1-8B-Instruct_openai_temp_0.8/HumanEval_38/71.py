### Cyclic Encoding and Decoding Script
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): input string to be encoded
    
    Returns:
    str: encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): input string to be decoded
    
    Returns:
    str: decoded string
    """
    # initialize the decoded string
    decoded_str = ""
    char_index = 0
    # loop through the encoded string in steps of 3
    while char_index < len(s):
        # get the current group of three characters
        group = s[char_index:char_index+3]
        # if the group has 3 characters, cycle them
        if len(group) == 3:
            decoded_str += group[1:] + group[0]
        # if the group has fewer than 3 characters, append it as is
        else:
            decoded_str += group
        char_index += 3
    return decoded_str


# Example usage:
if __name__ == "__main__":
    # Test the functions
    original_string = "abcdefghij"
    print(f"Original String: {original_string}")
    
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded String: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")

```
In this script, the `encode_cyclic` function takes a string and encodes it by cycling groups of three characters. The `decode_cyclic` function takes an encoded string and decodes it by reversing the process used in `encode_cyclic`. The example usage demonstrates how to use these functions with a test string.