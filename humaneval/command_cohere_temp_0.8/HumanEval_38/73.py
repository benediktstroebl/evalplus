```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3. 
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group in reverse. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups[::-1]]
    return "".join(groups)
```

The `encode_cyclic` function splits the input string into groups of three characters, and then cycles each group; reordering its characters. This generates an encoded string. The `decode_cyclic` function performs the inverse operation, splitting the encoded string into groups of three characters, and then cycling each group in reverse to recover the original string. These functions are designed to handle any string length, and effectively convert between plain text and encoded representations.