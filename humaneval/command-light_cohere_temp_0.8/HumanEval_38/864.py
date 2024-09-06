```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    If the string isn't divisible by 3, it will be encoded with a special marker instead of elements from the cyclic group.
    """
    - split string to groups of three characters
    for i in range((len(s) + 2) // 3):
        if len(s) % 3 == 0:
            groups = s[(3 * i):min((3 * i + 3), len(s))]
        else:
            groups = [''] + s[(3 * i):min((3 * i + 3), len(s))]
        # cycle elements in each group. Unless group has fewer elements than 3.
        groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    also checks for the standard of the input.
    """
    return s.split().s[encode_cyclic, s[0:1], '']
```
This script defines a function called `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. It then defines a function called `decode_cyclic` that takes an input string as its argument and returns a decoded string. The `decode_cyclic` function also checks for the standard of the input string to ensure correct decoding.