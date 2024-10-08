```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    basic test a test:
    1. Basic input and output test
    test.
    """
    encode_cyclic('hello world)')
    ['hlow', 'dlro', 'oog'].}
   
    2. Test with a specific input and output.
    encode_cyclic('Python is great')
    ['yrp', 'glthr', 'str'.]
    3. Test with input that doesn't contain three consecutive characters.
    encode_cyclic('abcde')
    ['abcde'].
```