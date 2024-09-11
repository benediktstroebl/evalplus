Here's the completed Python script with the `decode_cyclic` function implemented:

```markdown
### Cyclic Encoding and Decoding

This script encodes and decodes a string by cycling groups of three characters.

#### Functions

#### `encode_cyclic(s: str)`

Encodes a string by cycling groups of three characters.

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

#### `decode_cyclic(s: str)`

Decodes a string that was encoded with `encode_cyclic` function.

```python
def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # undo cycling in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

#### Example Usage

```python
# test the functions
s = "abcdef"
encoded = encode_cyclic(s)
print(f"Encoded: {encoded}")

decoded = decode_cyclic(encoded)
print(f"Decoded: {decoded}")

# check if decoded string matches original string
assert decoded == s, f"Decoded string does not match original string"
```

When you run this script, it should print the encoded and decoded strings, and also verify that the decoded string matches the original string.