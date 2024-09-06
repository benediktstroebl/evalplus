```python
def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group.
    groups = [group[1:] + group[0] for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Reverse the encoding process.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    return "".join(group[0] + group[1:] for group in groups)
```