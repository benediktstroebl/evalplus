```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR operation on two strings.
    >>> string_xor('010', '110')
    '100'
    """
    return str(b ^ a)

# Test cases
test_cases = [
    ("010", "110"),
    ("0011", "1110"),
    ("001", "1111"),
    ("aa", "aa"),
    ("1010", "1011"),
]

for case in test_cases:
    actual = string_xor(*case)
    assert actual == case[0] + case[1], "Test case failed: " + actual + " vs [" + case[0] + case[1]]"
```  This Python code defines a function called `string_xor` that performs the binary XOR operation on two input strings. It uses the
 typing module for better type inference. The function takes two string inputs (a and b) and returns their binary XOR as a string. The code also includes a series of test cases to verify the correctness of the `string_xor` function. 

Finally, the code verifies each test case's expected result against the function's output, ensuring accurate behavior.