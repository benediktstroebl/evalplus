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
    result = ""
    temp = ""
    for char in s:
        temp += char
        if len(temp) == 3 or (len(temp) == 2 and (len(s) - len(temp)) % 3 == 0):
            # cycle elements in each group
            if len(temp) == 3:
                result += temp[1] + temp[0] + temp[2]
            else:
                result += temp[1] + temp[0]
            temp = ""
    if temp:
        result += temp
    return result


# Example usage
s = "abcdefghi"
encoded = encode_cyclic(s)
print(f"Encoded string: {encoded}")

decoded = decode_cyclic(encoded)
print(f"Decoded string: {decoded}")
```

In this code, we define the `encode_cyclic` function to encode a string by cycling groups of three characters, as specified. We then define the `decode_cyclic` function to decode a string that was encoded with `encode_cyclic`. The decoding function works by iterating over the encoded string and adding characters to a temporary string until it has three characters or two characters (at the end of the string). It then cycles the elements of the temporary string and adds it to the result string. Finally, we demonstrate the usage of both functions with an example string.