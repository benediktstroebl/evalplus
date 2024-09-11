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
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode elements in each group. Unless group has more elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Testing the functions
if __name__ == "__main__":
    test_string = "HelloWorld"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, to encode and decode a string by cycling groups of three characters. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and joins them back into a string. The `decode_cyclic` function does the reverse operation to decode the string. The script includes a test case to demonstrate the usage of these functions.