```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    watched input string encoded with encode_cyclic function. Returns decoded string.
    """
    report, error if input is not correctly encoded
    """
    assert "".join(encode_cyclic(s), "Input is not correctly encoded")
    return decode_cyclic(s)

# Example usage
print(encode_cyclic("hello world")) # encoded
print(decode_cyclic("hello world")) # decoded
```
This code defines a self-contained function that solves the given problem. It takes two input string and returns the decoded string, or raises an error if the input is not correctly encoded.