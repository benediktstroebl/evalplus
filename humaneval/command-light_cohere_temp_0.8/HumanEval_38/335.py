```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    The string is split into groups of three characters
    each of these groups will be cycled, meaning the first character will be the last in the returned string
    s[:len(s) // 3] = s[1::3] = s[2::3] = ...
    return s[:len(s) // 3] + s[len(s) // 3 + 1:]

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    takes as input string decoded with encode_cyclic function.
    Returns the string decoded
   
```
This Python script defines a function called `encode_cyclic` that converts an input string `s` into an encoded version by cyclically cycling groups of three characters. The function also includes a test that checks if the encoded string matches the output of the `encode_cyclic` function applied to the input string. The `decode_cyclic` function takes the encoded string as input and returns the decoded version of the string, which is the original string with the groups of three characters recombined.