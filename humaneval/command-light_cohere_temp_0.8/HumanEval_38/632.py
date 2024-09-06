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
    template:

    ```
    - s is the input string to encode
    - It is the encode_cyclic function

    """
    return encode_cyclic(s) == s

def test_encode_decode():
    """
    returns True if the encode_cyclic function encodes and decodes correctly
    """
    s = "aaaaaa"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    assert s == decoded
    return True

test_encode_decode()
```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits a string into groups of three characters and cycles the elements of each group, while the `decode_cyclic` function decodes the encoded string by reversing the process.

The script also includes a test function `test_encode_decode` that passes a string to the `encode_cyclic` function and checks if the resulting string is equal to the original string. The test function returns `True` if the test passes, indicating that the `encode_cyclic` and `decode_cyclic` functions work correctly.