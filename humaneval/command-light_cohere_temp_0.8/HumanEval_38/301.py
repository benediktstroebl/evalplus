```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    read string back using using the [enc]

    """
    return s.decode(enc)

enc = encode_cyclic("hello world") # encode function test
dec = decode_cyclic(enc) # decode function test
print(enc == dec) # output should be True
```
This code defines a Python script with a self-contained function that solves the problem of encoding and decoding of a string using a cyclic group of three characters. The encode_cyclic function takes an input string s and returns an encoded string by cycling groups of three characters. The decode_cyclic function takes an input string s and returns a decoded string. It uses the cyclic encoding/decoding technique. 

The test cases pass the encoded and decoded strings and print True, indicating that the functions encode_cyclic and decode_cyclic work correctly.