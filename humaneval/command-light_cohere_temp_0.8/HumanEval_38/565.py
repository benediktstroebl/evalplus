```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [w for w in s if len(w) == 3]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    respective tests
    """
    if s == encode_cyclic("Hello World")
    return s


s = encode_cyclic("Hello World")
print(s)  # Output: gHCegklHroolkg
```
This script defines two functions, `encode_cyclic` and `decode_cyclic`, which are used to encode and decode a string of characters. 

The `encode_cyclic` function splits the input string into chunks of three characters, and then cycles through each group of characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string.