```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3. Each of the groups of characters.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    an input string is encoded with encode_cyclic function.
    # decode the a string.
    # split string to groups of characters
    groups = s.split("". group[:3] + " " + group[3:] for group in s.group[0:3] for group in s.
    return "".join(groups)

# test cases
print(encode_cyclic("hello"))
print(encode_cyclic("h" + "e" + "l" + "l" + "o"))
print(encode_cyclic("Python" + "_" + " coding "))
print(decode_cyclic("Python_coding"))
print(decode_cyclic("python_coding"))
```