```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   aya decoded string.
    encoded = encode_cyclic(s)
    return s.decode(encoded)

```
This Python script defines a self-contained function called `encode_cyclic` that encodes a given string by creating groups of three characters and cycling them. The `decode_cyclic` function is defined to take an encoded string as input and return the decoded string. The encode_cyclic function utilizes the `groups` variable to split the string into groups of three characters, while the `decode_cyclic` function utilizes the encode_cyclic function to convert the encoded string back to its original decoded format.