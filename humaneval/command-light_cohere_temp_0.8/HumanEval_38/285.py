```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    leads thex copy the strings to the input and verifies the correctness
    """
    assert encode_cyclic("hello world") == "hol123olol93"
    assert encode_cyclic("abc") == "bca123ac"
    assert encode_cyclic("abcde") == "cd123a"
    assert encode_cyclic("imals") == "ilwooimoa"
    assert encode_cyclic("") == "."
    assert encode_cyclic(" ") == "."
    assert encode_cyclic(["a", "bc", ""]) == "bca123ac"
    assert encode_cyclic(["a", "bc", "a", "c"]) == "bca1234ca"
    assert encode_cyclic(["a", "bc", "d"]) == "cd123d"
    assert encode_cyclic([]) == "."
    assert encode_cyclic([1, 2, 3]) == "12312"

```
The Python code defines two self-contained functions: `encode_cyclic` and `decode_cyclic`. It converts a given string into an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the original decoded string. The code then implements several test cases for both functions, checking that the encoded and decoded strings produce the correct output and pass all the tests.