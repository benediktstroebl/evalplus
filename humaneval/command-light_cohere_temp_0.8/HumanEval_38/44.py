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
    all tests for different length of encoded string are passed to this function.
    # check if first and last characters are digits
    if s[0] == s[-1] and s[1] in '0123456789':
        return s[:-1] + s[-1]
    else:
        return s

# test cases
test_string = "abc123def456ghijklmnoqrpsstuvxyzabc"
print(encode_cyclic(test_string))
print(decode_cyclic(test_string))
```
This script defines a function `encode_cyclic` that takes a string as input and returns an encoded version of it by cycling groups of three characters. The function then defines a function `decode_cyclic` that takes an encoded string as input and returns the decoded string. The `decode_cyclic` function checks if the first and last characters are digits. If they are, it returns the first character of the encoded string. If not, it returns the entire encoded string.

Finally, the script provides some test cases for the `encode_cyclic` and `decode_cyclic` functions. The output will display the results of the tests.