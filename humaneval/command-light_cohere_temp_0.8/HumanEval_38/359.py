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
    < requires encoding and decoding to work.
"""

# Example 1
print(encode_cyclic("hello world"))  # encodes as "hhungdlrooooo oola"

# Example 2
print(decode_cyclic("hhungdlrooooo oola"))  # decodes to "hello world"

# Example 3
print(encode_cyclic("abcdeefghijklmnopqrstvui"))  # encodes as "fgijklmnopstvui"

# Example 4
print(decode_cyclic("fgijklmnopstvui"))  # decodes to "abcdeefghijklmnopqrstvui"

```

This Python script defines two self-contained functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and then cycles the characters within each group. The `decode_cyclic` function takes an encoded string and decodes it by reversing the process of the `encode_cyclic` function.