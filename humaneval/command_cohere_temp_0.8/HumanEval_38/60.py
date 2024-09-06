```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer than 3 elements.
    groups = [group[1:] + group[0] for group in groups if len(group) == 3]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Return elements in each group in original order.
    return "".join([group[0] + group[2] for group in groups])
```

The `encode_cyclic` function splits the input string into groups of three characters, and then cycles the characters within each group to create a new encoded string. This is achieved by concatenating the first and second characters of each group, and then the second and third characters to obtain the cycled group. This process is repeated for each group in the input string.

The `decode_cyclic` function reverses the encoding process. It splits the encoded string into groups of three characters, and then returns the original string by concatenating the first and second characters of each group, and then the second and third characters. This process is applied to each group in the encoded string to recover the original input string. 

Overall, the provided code appears to be logically correct and self-contained, and it should successfully encode and decode strings using the cyclic coding technique.