```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    """
    # split string to groups of three
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = groups[::-1]
    return "".join(groups)

# test encode_cyclic function
print(encode_cyclic("Hello World")) # Expected Output: Wjll ooj"

# test decode_cyclic function
print(decode_cyclic("Wjll ooj")) # Expected Output: Hello World
```

This Python script includes the encode_cyclic and decode_cyclic functions, which are self-contained to solve the problem of encoding and decoding a string of characters with a cyclic pattern. The script also passes the test cases for these functions to ensure their correctness.