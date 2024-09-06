```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    interest with the decoding string returned by encode_cyclic function.
    """
    test if decode_cyclic(encode_cyclic("hello world"))
    return "hello world"
```
This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits a given string into groups of three characters and cycles the characters in each group. The `decode_cyclic` function takes an encoded string and returns the decoded string by reversing the encoding process.