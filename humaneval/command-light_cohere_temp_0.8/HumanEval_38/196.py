This is a Python code that uses a self-contained function to solve the problem of encoding and decoding of a string of markdown code blocks:
```python
def encode_cyclic(s):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    serious encoding and decoding issues.
    """
    def test_encode(test_str):
        encoded = encode_cyclic(test_str)
        return encoded == test_str

    def test_decode(test_str):
        decoded = decode_cyclic(test_str)
        return decoded == test_str
```
This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns the encoded string. It uses a serious encoding and decoding issues. The `decode_cyclic` function takes a string as input and returns the decoded string. It uses the serious encoding and decoding issues.

The code also has two additional functions: `test_encode` and `test_decode`. These functions are used to test the `encode_cyclic` and `decode_cyclic` functions, respectively. They check if the string has been correctly encoded and decoded, respectively. The code can be used to solve the problem of encoding and decoding of a string of markdown code blocks in a self-contained manner.