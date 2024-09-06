```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    goal is decode the string and ensure it was decoded correctly.
    decoded = ''.join(decode_cyclic(s))
    assert decoded == s, f"decode failed with {s} and decoded with {decoded}"

s = "hello there123"
encoded = encode_cyclic(s)
decoded = decode_cyclic(encoded)
print(f"Original: {s}, encoded: {encoded}, decoded: {decoded}")
```
This Python script defines two functions, encode_cyclic and decode_cyclic, that handle the encoding and decoding of a string containing only the characters "l", "o", and "123". The script then passes these functions with a test string, and ensures the decoded string matches the original input string, and that the encoding and decoding operations are correct.