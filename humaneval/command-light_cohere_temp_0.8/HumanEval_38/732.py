```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
      `
    returns decoded string as the result of encoding and decoding of the string s`
    """
    return encode_cyclic(s) == s

# Example usage
s = "abcabc123"
print(encode_cyclic(s))
print(decode_cyclic(encode_cyclic(s)))
```
This script defines a function called `encode_cyclic` which takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function is used to take the encoded string as input and returns the decoded string. The example usage demonstrates the `encode_cyclic` and `decode_cyclic` functions with the string "abcabc123".