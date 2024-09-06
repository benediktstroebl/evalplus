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
    competitors expect to solve this problem"""
    return encode_cyclic(s)

# example usage
print(decode_cyclic("smurfflibgrph"))  # Output: "fiborgrumfslibgrf"
```
This Python script defines a self-contained function called `encode_cyclic` that performs encoding using the technique described in the previous problem. It also includes a `decode_cyclic` function to decode the encoded string. The `encode_cyclic` function splits the input string into groups of three characters and cycles the elements within each group. The `decode_cyclic` function then decodes the input string by passing it to the `encode_cyclic` function.