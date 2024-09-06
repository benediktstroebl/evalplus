```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
   
      other functions to test it's correctness.
}

print(encode_cyclic("hello"))
print(encode_cyclic("helo"))
print(encode_cyclic("helooo"))
print(encode_cyclic("hello world"))
print(decode_cyclic("hello"))
print(decode_cyclic("helo"))
print(decode_cyclic("helooo"))
print(decode_cyclic("hello world")))
```

This code defines a function `encode_cyclic` which takes a string `s` as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function is used to take the encoded string as input and returns the decoded string.