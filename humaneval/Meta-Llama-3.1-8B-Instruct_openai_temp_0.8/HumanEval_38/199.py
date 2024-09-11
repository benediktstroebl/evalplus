```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # initialize an empty string to store the decoded result
    decoded_string = ""
    # initialize a counter to keep track of the current position in the string
    pos = 0
    # loop until we've processed the entire string
    while pos < len(s):
        # extract the next group of three characters
        group = s[pos:pos + 3]
        # if the group is shorter than three characters, pad it with the next character
        if len(group) < 3:
            if len(group) == 1:
                decoded_string += group + s[pos + 1]
            else:
                decoded_string += group + s[pos + 1]
        # if the group is equal to the last three characters of the original string, 
        # it means we've encountered the first group
        elif group == s[-3:]:
            # append the remaining characters to the decoded string
            decoded_string += s[pos:]
            break
        # if the group is not equal to the last three characters of the original string, 
        # it means we've encountered the last group
        else:
            # append the group to the decoded string, except for the last character, 
            # which is the first character of the group
            decoded_string += group[:-1] + group[-1]
        # move the position forward by three characters
        pos += 3
    return decoded_string


# example usage
original_string = "abcdef"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)
print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
```

This script first defines the `encode_cyclic` function, which cycles groups of three characters in the input string. Then it defines the `decode_cyclic` function, which takes the encoded string and returns the original string. Finally, it demonstrates the usage of these functions with an example.