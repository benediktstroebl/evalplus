### Cyclic Encoding and Decoding
#### Problem Description
The following Python script provides functions to encode and decode strings using a cyclic method.

#### Code

```markdown
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    :param s: string to be encoded
    :return: encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: encoded string
    :return: decoded string
    """
    # initialize result string
    result = ""
    # split string to groups of 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # join groups back into single string
    result = "".join(groups)
    return result


# example usage
encoded_str = encode_cyclic("abcdef")
decoded_str = decode_cyclic(encoded_str)

print("Encoded String: ", encoded_str)
print("Decoded String: ", decoded_str)
```

This script provides two main functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string by cycling elements in each group.

In the example usage section, we first encode a string using `encode_cyclic` and then decode the encoded string using `decode_cyclic`. The encoded and decoded strings are then printed to the console.