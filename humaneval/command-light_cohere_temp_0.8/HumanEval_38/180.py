```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
   
    """
    s = input()
    g = s[::3::i]
    return s[::3::i]
```
This Python script contains a self-contained function called `encode_cyclic` that encodes a given string by cycling groups of three characters. It also has a `decode_cyclic` function that takes an input string encoded with the `encode_cyclic` function and returns the decoded string.

The `encode_cyclic` function splits the input string into groups of three characters and cycles the elements within each group. It returns an HTML representation of the encoded string by joining the elements of each group back together.

The `decode_cyclic` function takes the input string and the previously encoded string, and returns the decoded string by inverting the encoding process.