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
    decoded_groups = []
    i = 0
    while i < len(s):
        group = s[i:i+3]
        if len(group) == 2:  # last group if string length is not divisible by 3
            decoded_groups.append(group[::-1])  # append reversed group
        else:
            decoded_groups.append(group[1:] + group[0])  # cycle elements in the group
        i += 3  # increment index by 3 for next group
    return "".join(decoded_groups)


# Testing the functions
if __name__ == "__main__":
    test_string = "abcdefghijkl"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script first defines the `encode_cyclic` function, which encodes a string by cycling groups of three characters. It then defines the `decode_cyclic` function, which takes as input a string encoded with `encode_cyclic` and returns the decoded string.

The `decode_cyclic` function works by iterating over the input string in groups of three characters. If a group has only two characters (which can occur if the string length is not divisible by 3), it appends the group in reverse order. Otherwise, it cycles the elements in the group by appending the elements after the first one to the first one. The decoded groups are then joined together to form the decoded string.