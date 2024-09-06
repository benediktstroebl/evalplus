```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(c for i, c in enumerate(s) if i % 3 == 0)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    result is same the result of encode_cyclic is expected to be the input string.
    """
    result of decode_cyclic is expected to be the decoded string
    """
    return encode_cyclic(s)

# Test cases
def test_encode_decode():
    assert encode_cyclic("hello") == "olleh"
    assert encode_cyclic("World") == "dlroW"
    assert encode_cyclic("!b.oay") == "d.S"
    adds test strings that have the same characters but are out of order, so you could get a False output from the assert.

def test_decode_Cyclic():
    assert decode_cyclic("olleh") == "hello"
    assert decode_cyclic("dlroW") == "World"

# Function call example
print(encode_cyclic("Python is great!"))

This script defines a self-contained function called `encode_cyclic` that takes a string s as input and returns an encoded version of the string. The `decode_cyclic` function takes an encoded string s as input and returns the decoded version of the string. The test_encode_decode function provides two test cases to verify the correctness of the `encode_cyclic` and `decode_cyclic` functions. The test_decode_Cyclic function provides additional test cases to validate the behavior of the `decode_cyclic` function.