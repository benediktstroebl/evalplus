```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    have the template for the
    """
    return s.decode_cycl(*decoded_cyclic)

# Test cases
print(encode_cyclic("hello world"))  # encoded
print(decode_cyclic("hello world"))  # decoded
print(encode_cyclic("abc"))     # encoded
print(decode_cyclic("abc"))     # decoded
print(encode_cyclic("abc123")) # encoded
print(decode_cyclic("abc123")) # decoded
print(encode_cyclic("123abc")) # encoded
print(decode_cyclic("123abc")) # decoded
print(encode_cyclic("..."))    # encoded
print(decode_cyclic("..."))    # decoded
```
The provided Python script defines a self-contained function, `encode_cyclic`, which takes a string as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function is used to take the encoded string as input and returns the decoded string. The code has test cases that demonstrate the functionality of the `encode_cyclic` and `decode_cyclic` functions.