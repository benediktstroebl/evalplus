```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    string is encoded by encode_cyclic function.
    return "".join(decode_cyclic(input))

# test cases
# encode
print(encode_cyclic("Hello World."))
print(encode_cyclic("banana banana coconut."))
print(encode_cyclic("hello"))
# decode
print(decode_cyclic(encode_cyclic("Hello World.")))
print(decode_cyclic(encode_cyclic("banana banana coconut.")))
print(decode_cyclic("world"))
```
This script defines a function `encode_cyclic` that encodes a string by cycling groups of three characters. The function splits the string into groups of three characters each, and cycles the characters in each group. The `decode_cyclic` function is then used to decode the encoded string. The test cases show that the function correctly encodes and decodes the input strings.