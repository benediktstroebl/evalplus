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
    guess the problem
 print(decode_cyclic(encode_cyclic("TestString"))))  # Returns "TestString"
    print(decode_cyclic(encode_cyclic("aaaaaaattc SerIIIsikT!")))  # Returns "SerIIIsikT!"
    print(decode_cyclic(encode_cyclic("Help me . A B C")))  # Returns "Help a b c"
    print(decode_cyclic(encode_cyclic("1234...")))  # Returns "1234"
    print(decode_cyclic(encode_cyclic("gggg")))  # Returns "gggg"
    print(decode_cyclic(encode_cyclic("aaaa-aaaaaaattc SerIIIsikT!")))  # Returns "SerIIIsikT!"
```
This script defines the `encode_cyclic` function that takes a string `s` as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function is used to take the encoded string as input and return the decoded string.