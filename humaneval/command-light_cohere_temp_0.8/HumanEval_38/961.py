```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return r".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    o !
    # encoded string contains cycles of three characters, each represented as a list of characters.
    """
    # split string to groups of length 3
    groups = s[::3].strip()
    decoded = ""
    for i, group in enumerate(groups):
        decoded += group[0]
    return decoded
``` 
This code contains two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns an encoded string. The encoded string contains cycles of three characters, each represented as a list of characters. The `decode_cyclic` function takes an encoded string as input and returns a decoded string. It uses a to split the input string into groups of length 3, then appends the first character of each group to the decoded string. 

Note that this solution uses the built-in string slicing method `::3` to split the input string into groups of length 3, and then uses the `strip` method to remove any whitespace characters from each group.