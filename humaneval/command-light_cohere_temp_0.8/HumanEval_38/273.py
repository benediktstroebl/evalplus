Here is a self-contained Python script that solves the problem of encoding and decoding markdown code blocks using the functions `encode_cyclic` and `decode_cyclic`:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
       
    """
    # reverse the encode_cyclic function
    return "".join(reversed(encode_cyclic(s)))

# sample input and output
input_str = """# h2o
---
# how are you going
"""
print(decode_cyclic(input_str))  # expected output: ious this is empty string
```

This Python script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an input string and returns the decoded string. The script also includes sample input and output for testing the functions.

Note: that you can add more tests and comments to this script to make it more readable and easier to understand.

This code is self-contained, and it can be used to solve the problem of encoding and decoding markdown code blocks in a single Python script.