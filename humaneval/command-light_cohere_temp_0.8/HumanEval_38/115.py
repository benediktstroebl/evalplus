```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    dry decode string
   
        """
    return s.remove(''.encode_cyclic'
```

The code defines a function `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. It achieves this by splitting the string into groups of length three, cycling elements in each group, and then joining the elements back together. The code also defines a function `decode_cyclic` that takes an input string and returns a decoded string. It uses the `encode_cyclic` to decode the input string.