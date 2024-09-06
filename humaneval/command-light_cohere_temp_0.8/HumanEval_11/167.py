```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only digits 1 and 0.
    """
    Result: 1010
    """
    return ''.join(str(ord(a[i]) ^ ord(b[i]) for i in range(len(a)))

# Test cases
test_string_xor = [("010", "110"), ("001", "101"), ("000", "111"), ("001", "101")]

for test in test_string_xor:
    actual = string_xor(*test)
    assert actual == test[0] + test[1], "Test case failed: " + str(actual) + " != " + str(test[0]) + " " + str(test[1])

```
The provided code includes a function `string_xor` that takes two input strings consisting only of digits 1 and 0, and performs the XOR operation to generate a new string. It then defines a test cases, where the function is invoked with different pairs of strings and verifies if the result matches the expected output. 
By using the asserts, it validates if the function is working correctly for each test case.