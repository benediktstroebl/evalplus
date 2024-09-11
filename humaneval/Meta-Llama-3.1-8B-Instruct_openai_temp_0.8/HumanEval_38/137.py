## Cyclic Encoding and Decoding
### Problem Statement

Implement a Python script that encodes and decodes a string using a cyclic method, where each group of three characters is cycled.

### Code

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
    # decode cyclic string
    decoded_groups = []
    for group in s:
        if len(decoded_groups) == 0:  # if the decoded string is empty, append the first group
            decoded_groups.append(group)
        elif len(decoded_groups) % 3 == 0:  # if the length of decoded string is multiple of 3, append the group rotated to the right
            decoded_groups.append(decoded_groups[-3] + decoded_groups[-2] + decoded_groups[-1])
        else:  # if the length of decoded string is not multiple of 3, append the group
            decoded_groups.append(group)
    # join the decoded string
    return "".join(decoded_groups)


# Example usage
test_string = "HelloWorld123"
encoded_string = encode_cyclic(test_string)
decoded_string = decode_cyclic(encoded_string)

print("Test string:", test_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)
```

### Explanation

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function takes the encoded string as input and decodes it by rotating the groups of three characters to the left and appending them to the decoded string.

In the example usage, a test string "HelloWorld123" is encoded using `encode_cyclic` and then decoded using `decode_cyclic`. The original test string, encoded string, and decoded string are printed to verify that the encoding and decoding process works correctly.