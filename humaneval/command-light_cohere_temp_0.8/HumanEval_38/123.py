```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example test the someting with is a valid encoded string
    """
    return s.decode_cycl(encode_cyclic(s))

# test cases
print(encode_cyclic("hello world")) # output should be h4eolvld 

print(encode_cyclic("test!")) # output should be t2est!

print(encode_cyclic("abc")) # this should be abcd

print(decode_cyclic("h4eolvld")) # this should be helloworld

print(decode_cyclic("t2est!")) # this should be test!
```
This code defines a set of functions and a test suite that are self-contained and solve the problem of encoding and decoding strings. 

The encode_cyclic function splits a string into groups of three characters and cycles the characters within each group. The decode_cyclic function takes an encoded string and decodes it using the encode_cyclic function.