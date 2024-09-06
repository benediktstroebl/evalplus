```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    If input string is not of length divisible by three, raise ValueError.
    If the string has groups of three characters, encode them in a cyclic manner.
    If the string has less than three characters, return it as is.
    Return the result as a list of encoded strings.
    """
    return ["".join([group[0] + group[1:] + group[2] if len(group) == 3 else group for group in s[(3 * i):min((3 * i + 3), len(s))]] for i in range((len(s) + 2) // 3)]

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    The verity-check: decoded string is the same as original string.
    return s
 verity-check: decoded string is the same as original string
    """
    return encode_cyclic(s) == s

# run the test suite to check if the functions are working as expected
```