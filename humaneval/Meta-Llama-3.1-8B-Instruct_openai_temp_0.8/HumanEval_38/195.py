```markdown
### Cyclic Encoding and Decoding Script

This script provides functions for encoding and decoding a string using a cyclic pattern.

#### encode_cyclic function

Encodes a string by cycling groups of three characters.

#### decode_cyclic function

Decodes a string that was previously encoded using the encode_cyclic function.
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
        s (str): encoded string to be decoded
    
    Returns:
        str: decoded string
    """
    # initialize an empty string to store decoded string
    decoded = ""
    # initialize a counter to track current position in the string
    i = 0
    while i < len(s):
        # if current character is not last in string
        if i + 2 < len(s):
            # decode group by moving first character to the end
            decoded += s[i + 1:i + 3] + s[i]
            # increment counter by 3
            i += 3
        else:
            # if current group has fewer than 3 characters, append it to decoded string
            decoded += s[i:]
            # break out of loop since we've processed the entire string
            break
    return decoded


# Test the functions
input_str = "abcdefghij"
encoded_str = encode_cyclic(input_str)
decoded_str = decode_cyclic(encoded_str)

print(f"Input String: {input_str}")
print(f"Encoded String: {encoded_str}")
print(f"Decoded String: {decoded_str}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which can be used to encode and decode a string using a cyclic pattern. The `encode_cyclic` function splits the input string into groups of three characters, and then cycles the elements in each group. The `decode_cyclic` function reverses this process by moving the first character of each group to the end.

The script also includes a test case to demonstrate how to use these functions. The test case encodes and decodes the string "abcdefghij" and prints the results.