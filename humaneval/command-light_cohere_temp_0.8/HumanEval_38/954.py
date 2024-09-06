```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    #
    time encoded string and returns decoded string
    """
    return s

# Test cases
print(encode_cyclic("hello world"))
print(encode_cyclic("hello world banana"))
print(encode_cyclic("hello world! my name is Carl"))
print(decode_cyclic(encode_cyclic("hello world")) )
print(decode_cyclic(encode_cyclic("hello world banana")) )
print(decode_cyclic(encode_cyclic("hello world. my my name is Carl"))
```
This script has two functions: `encode_cyclic` encodes a string into a markdown code block and `decode_cyclic` decodes a string from a markdown code block.  The test cases to ensure the function is correct.