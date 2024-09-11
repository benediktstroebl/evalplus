### Cyclic Encoding and Decoding

Here is a Python script that provides a self-contained implementation of the cyclic encoding and decoding functions:

```markdown
### Cyclic Encoding and Decoding

#### Usage

```python
encoded = encode_cyclic("hello")
decoded = decode_cyclic(encoded)
print(decoded)  # prints "hello"
```

#### Code

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


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    def rotate(group):
        if len(group) == 3:
            return group[-1] + group[:-1]
        return group

    return "".join([rotate(group) for group in (s[i:i+3] for i in range(0, len(s), 3))])
```

#### Explanation

The `encode_cyclic` function works by splitting the input string into groups of three characters. It then rotates each group by one position unless the group has fewer than three characters. The `decode_cyclic` function works by rotating each group of three characters back by one position. It uses a helper function `rotate` to rotate the groups.

Note: The decoding function uses list comprehension to rotate each group of three characters in the encoded string. It also uses slicing to create groups of three characters from the encoded string.