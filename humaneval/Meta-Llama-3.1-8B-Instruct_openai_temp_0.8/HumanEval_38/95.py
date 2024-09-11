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
    # check if string length is a multiple of 3, if so split the string into groups
    if len(s) % 3 == 0:
        groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    else:
        # if string length is not a multiple of 3, split it into groups and add the remaining characters at the end of the previous group
        groups = [s[:3]]
        for i in range((len(s) - 3) // 3 + 1):
            groups.append(s[(i * 3 + 3):min(((i + 1) * 3 + 3), len(s))])
        groups.append(s[len(s) - len(s) % 3:])

    # decode each group by moving the first character to the end
    return "".join([group[1:] + group[0] for group in groups])


# test the functions
if __name__ == "__main__":
    test_string = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = encode_cyclic(test_string)
    print("Encoded string:", encoded_string)
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
    print("Test passed" if test_string == decoded_string else "Test failed")
```

This script first defines the `encode_cyclic` function that takes a string as input and returns the encoded string by cycling groups of three characters. It then defines the `decode_cyclic` function that takes an encoded string as input and returns the decoded string by moving the first character of each group to the end.

In the `if __name__ == "__main__":` block, it tests the functions by encoding a string, decoding the encoded string, and checking if the decoded string is equal to the original string. If the test passes, it prints "Test passed", otherwise it prints "Test failed".