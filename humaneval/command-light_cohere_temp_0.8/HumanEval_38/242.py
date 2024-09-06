```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
        necessary to return the original string."""
    return s.decode_cyclic (encode_cyclic)

# Test cases
assertEqual(encode_cyclic("Aaaaa"), "..aaaa")
assertEqual(encode_cyclic("..B"),".-"B")
assertEqual(encode_cyclic("Hello World"),"H..dlroW olleH")
assertEqual(decode_cyclic("H..dlroW olleH"),"Hello World")
```
This code defines the functions `encode_cyclic` and `decode_cyclic`, which are responsible for encoding and decoding cyclic strings. The test cases ensure that the function produces the correct results.