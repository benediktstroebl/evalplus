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
    # Replace every group of three characters (that wasn't split in the encoding process) 
    # to be a rotation of the original group. Since groups where split if they had length less than 3.
    # we need to handle every group of length 3 as if it had length 4, by adding a character that we will then remove 
    # once we've decoded the string.
    decoded = "".join([group[1:3] + group[0] + group[3] if len(group) >= 3 else group for group in [s[i:i+3] for i in range(0, len(s), 3)]])
    # remove the extra character added in encoding process
    return decoded.replace(' ', '')


# Test the functions
original_string = "abcdefgh"
encoded = encode_cyclic(original_string)
decoded = decode_cyclic(encoded)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded}")
print(f"Decoded String: {decoded}")
```
Note: In the `decode_cyclic` function, we're adding a character to the end of each group (if the group has length 3 or more) to simulate a rotation of the group and handle the case where a character was removed in the encoding process. We then remove this character at the end of the decoding process.