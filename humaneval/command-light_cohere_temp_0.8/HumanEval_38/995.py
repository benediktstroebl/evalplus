Here is a Python script that solves the problem:

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    guessing that encode_cyclic function.
    """
    open_string = ''.join(encode_cyclic(s))
    return decode_cyclic(open_string)

# test cases
print(encode_cyclic("hello world"))
print(encode_cyclic("hello"))
print(encode_cyclic("h"))
print(encode_cyclic(""))
print(decode_cyclic("hello world"))
print(decode_cyclic("hello")))
print(decode_cyclic("h"))
print(decode_cyclic(""))
```

The script defines two functions, `encode_cyclic` and `decode_cyclic`, which are used to encode and decode a string, respectively. The `encode_cyclic` function takes a string as input and returns an encoded version of the string, where the characters are split into groups of three characters. The `decode_cyclic` function takes a string as input and returns the original string, which can be guessed by passing the encoded string back to the `encode_cyclic` function.