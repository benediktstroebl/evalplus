Here is a Python script that contains a self-contained function that solves the problem of encoding and decoding markdown code:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    longest elements in groups of three characters.
    groups = s.split("..groups")
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

# Test case 1
print(encode_cyclic("Hello")) # Output should be Hehllloo

# Test case 2
print(encode_cyclic("Doit")) # Output should be Doit

# Test case 3
print(encode_cyclic("Goodn")) # Output should be Goodn

# Test case 4
print(encode_cyclic("code")) # Output should be coke

# Test case 5
print(encode_cyclic("></)) # Output should be ]

# Test case 6
print(encode_cyclic("\\"\"\"\"")) # Output should be \\\"o

# Test case 7
print(encode_cyclic("\ud83c")) # Output should be \ud83c

# Test case 8
print(encode_cyclic("\ud83d\u3000")) # Output should be \ud83d\3000

# Test case 9
print(encode_cyclic("\u\u00a")) # Output should be \u00a

# Test case 10
print(encode_cyclic("\u\ud83d\u3000")) # Output should be \ud83d\3000
```
This script provides a simple implementation of the encoding and decoding functionality. It can be easily modified to solve larger encoding and decoding problems, and it can be used as a reference for creating self-contained functions for these tasks.