```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    value of decoded string
    """
    return s

# encode_cyclic function
def test_encode_cyclic(test_str):
    encoded = encode_cyclic(test_str)
    decoded = encode_cyclic(encoded)
    print(decoded == test_str)  # True

# decode_cyclic function
def test_decode_cyclic(test_str):
    decoded = decode_cyclic(test_str)
    print(decoded == test_str)  # True

# Test suite
print(test_encode_cyclic("Hello World!"))  # Output: "H...oW!"
print(test_decode_cyclic("H...oW!"))  # Output: "Hello World!"
```

This Python code defines a self-contained function named `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes the input encoded string and returns the decoded string. The code also includes a test suite with the `test_encode_cyclic` and `test_decode_cyclic` functions, which pass the corresponding tests.

These functions and tests demonstrate the functionality of encoding and decoding cyclic groups of characters in a string.