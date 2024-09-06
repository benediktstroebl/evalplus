```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer than 3 elements.
    groups = [group[1:] + group[0] if len(group) < 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Undo the rotation.
    groups = [group[0] + group[2:] if len(group) < 3 else group for group in groups]
    return ''.join(groups)
```

The `encode_cyclic` function splits the input string into groups of three characters, then cycles the elements within each group to produce a new string. This process is repeated until the last group, which contains fewer than three characters, is handled gracefully by simply returning it without modification. 

The `decode_cyclic` function effectively undoes the encoding process by splitting the input string into groups of three characters and then rotating the first and second groups to restore the original string. Finally, both functions join their respective groups back into a single string for output. 

These functions enable reliable encoding and decoding of strings using a cyclic encoding approach, ensuring data integrity throughout the encoding and decoding operations.