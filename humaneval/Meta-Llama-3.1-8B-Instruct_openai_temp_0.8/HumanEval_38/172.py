### Cyclic Encoding and Decoding
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # split string to groups. Each of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    decoded_string = ""
    # initialize index
    i = 0
    # loop through string in steps of 3
    while i < len(s):
        # get a group of three characters
        group = s[i:i + 3]
        # if group has less than three characters, use a loop to shift the remaining elements
        if len(group) < 3:
            group = group + s[i + len(group):] * ((3 - len(group)) % len(group)) + s[i + len(group):][: (3 - len(group))]
        # shift elements in group, unless it has fewer elements than 3
        if len(group) == 3:
            decoded_string += group[1] + group[0] + group[2]
        else:
            decoded_string += group
        # move to the next group
        i += 3
    return decoded_string


# Test the functions
if __name__ == "__main__":
    test_string = "abcdefghij"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
    print(f"Is the decoded string the same as the original string? {decoded_string == test_string}")
```
This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, and includes some example usage and testing code to demonstrate their behavior.