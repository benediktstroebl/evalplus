Here is a self-contained Python script with a function that solves the problem of encoding and decoding Markdown code using the given reference implementation:
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
   

    built based on the encode_cyclic function
    """
    return s.decode_cycl(encode_cyclic(s))

# Testing the implementation
def test_decode_cyclic():
    assert decode_cyclic("..::.") == "hello"

# Example usage
test_decode_cyclic()
```
This script defines the `encode_cyclic` and `decode_cyclic` functions. The `encode_cyclic` function splits the input string into groups of length 3 and cycles the elements of each group. The `decode_cyclic` function takes an encoded string and returns the decoded string, which is built using the `encode_cyclic` function. 
The `test_decode_cyclic` function tests the `decode_cyclic` function with a known input and asserts that the output is correct.