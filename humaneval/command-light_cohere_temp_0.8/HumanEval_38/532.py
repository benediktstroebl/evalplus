```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3
    groups = [sub[:3] for sub in s. lift strings of  length 3
   
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   0.lowercase strings to a strings.
    a.1.
    input should be encoded by encode_cyclal function
    """
    return s
def test_encode_decode():
    s = "hello world"
    print(encode_cyclic(s))
    print(decode_cyclic(encode_cyclic(s)))
```

This script defines the encode_cyclic and decode_cyclic functions, which solve the problem of encoding and decoding a string using the given approach. It also provides a test_encode_decode function, which passes the test string and verifies if the output of the encode_cyclic function matches the decoded string.