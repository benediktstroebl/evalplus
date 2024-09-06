```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group, and leave groups of three or more elements unchanged
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    copy of s
    """
    return s.encode_cyclic

# Example usage
encoded = encode_cyclic("Hello World")
decoded = decode_cyclic(encoded)
print(f"Original: {encoded}, {decoded}
```

The provided code defines a pair of functions: encode_cyclic and decode_cyclic, that work together to implement a cyclic encoding and decoding of strings. The encode_cyclic function splits a string into groups of three characters and then cycles each group. The decode_cyclic function, on the other hand, takes the encoded string and returns the decoded string. These functions can be used to encode and decode strings that contain repetitive groups of three characters, like in a markdown code block.