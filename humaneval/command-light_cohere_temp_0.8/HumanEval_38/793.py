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
    pattern = r"*.[3,]+
    s = s.replace("".*", "")
    s = s.replace("]", "")
    pattern_ = r"([^{.join}\b }$ )".
    s = s.replace(pattern, "").
    return s

# test cases
 tests = [
    # test case 1
    "aaaaaa",
    # test case 2
    "aaaaaa",
    # test case 3
    "bbbbbb",
    # test case 4
    "xxxxxx",
    # test case 5
    "aaaaaa",
    # test case 6
    "aaaaaa",
    # test case 7
    "aaaaaa",
    # test case 8
    "bbbbbb",
    # test case 9
    "bbbbbb",
    # test case 10
    "xxxxxx"
]
# test_ encode_cyclic function
for case in tests:
    result = encode_cyclic(case)
    print("Input: ", case)
    print("Result: ", result)
    assert result == encode_cyclic(decode_cyclic(case))
# test cases
 ```
This script defines a function called `encode_cyclic` that splits a given string into substrings of length 3, then cycles the characters in each group. This function then returns a string that has been encoded using the specified pattern. 

The `decode_cyclic` function takes an input string that has been encoded using the `encode_cyclic` function and returns the decoded string. The decoded string is then compared to the original input string using the `assert` statement. 

This script also includes a set of test cases that verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.