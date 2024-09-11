```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    decoded_str = ""
    while len(s) >= 3:
        decoded_str += s[:2] + s[2:]
        s = s[3:]
    if len(s) == 2:
        decoded_str += s[1] + s[0]
    elif len(s) == 1:
        decoded_str += s
    return decoded_str


# Testing the functions
original_string = "HelloWorld"
encoded_string = encode_cyclic(original_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```

In this script, the `encode_cyclic` function splits the input string into groups of three characters each, cycles the elements in each group, and then joins them together.

The `decode_cyclic` function does the reverse by continuously removing the last three characters of the encoded string and adding them to the beginning until the string has fewer than three characters. If it has two characters, it rearranges them. If it has one character, it leaves it as it is.