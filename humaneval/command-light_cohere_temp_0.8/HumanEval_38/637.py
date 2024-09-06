```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    If the length of a group is less than 3, it is returned directly.
    """
    string = ""
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    for group in groups:
        if len(group) == 3:
            string += group[1:] + group[0]
        else:
            string += group
    return string

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    example:
    "abc" -> "aabb"
    "abcde" -> "abcd"
    """
    return s.encode_cycl(decode_cyclic(s))

# Example:
print(encode_cyclic("hello"))  # Output: h e ll o
print(decode_cyclic(encode_cyclic("hello")))  # Output: hello
```