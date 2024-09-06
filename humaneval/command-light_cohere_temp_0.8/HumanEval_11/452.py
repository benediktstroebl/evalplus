```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two input strings.
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")

    # Use XOR to combine the characters
    result = ''.join(c ^ b[i] for i, c in enumerate(a))

    return result

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "111"),
    ("00", "10"),
    ("1000", "0000"),
    ("1010", "0110"),
    ("110", "1110"),
]

for act, exp in test_cases:
    actual = string_xor(act, act)
    assert actual == exp, f"Test case [{act}] failed: {actual}"
```

This Python code defines a function `string_xor` that performs the binary XOR operation on two input strings. The function ensures that the strings have the same length, then, it iterates over the characters in both strings, XORing each pair of characters. The output string is formed by the XOR of the characters in the input strings. 

The code also includes a set of test cases, which are used to verify the correctness of the `string_xor` function. The test cases cover a scenarios, including different lengths of strings, input patterns, and edge cases. 
The code uses the `assert` statement to check if the actual output matches the expected output for each test case.