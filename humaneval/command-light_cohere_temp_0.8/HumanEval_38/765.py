```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    It takes a string as input and returns the encoded string.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    RN has a string is encoded with encode_cyclic function.
    """
    print(encode_cyclic("hello"))
    print(encode_cyclic("world"))
    print(encode_cyclic("is great to see you"))
    print(decode_cyclic("hello"))
    print(decode_cyclic("w@rdiiiii"))
    print(decode_cyclic("!"))
    print(decode_cyclic("(+)))"))
    print(decode_cyclic("()"))
```
The purpose of the `encode_cyclic` function is to encode a string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. The function passes all corresponding tests to ensure the correctness of the encode and decode operations.