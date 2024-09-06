```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g + s[i : i + 3] for i, g in enumerate((s[(3 * i):min((3 * i + 3), len(s))) for i in range((len(s) + 2) // 3))))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """

    test cases:
    1. s input string "abc...a" and prints "aabc".
    2. Decodes the strings of "aab...c" and prints "abc".
    3. Decodes "content with " = "aab..." and gets "aab...c".

```