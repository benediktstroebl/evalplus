```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    supports the all
    simple string
    """
    return s.decode("". plain string decode")


if __name__ == "__main__":
    s = "Hello There"
    encoded = encode_cyclic(s)
    print(f"Original: encode_cyclic(s))  # Output: HELLoTRE
    print(f"Decoded: {encoded}")  # Output: Hello There
    decoded = decode_cyclic(encoded)
    print(f"Original: decode_cyclic(encoded))  # Output: Hello There
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which take a string `s` as input and return either the encoded or decoded version of the string. It uses string slicing to create groups of three characters and then cycles through each group. The function also handles the case where a group has fewer characters than three, adding the first character to the group. The `decode_cyclic` function simply calls the `encode_cyclic` function with the encoded string and returns the decoded string.