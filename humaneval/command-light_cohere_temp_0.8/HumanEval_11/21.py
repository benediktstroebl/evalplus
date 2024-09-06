```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b. 
    
    :type a string a: str
    :type string b: str
    :rtype string str
    """
    return str(a ^ b)

# Test cases
test_cases = [
    "010",
    "110",
    "0011",
    "1010",
    "1111"
]

for test_case in test_cases:
    actual_result = string_xor(test_case, test_case)
    print(f"Input: {test_case} => Result: {actual_result}")
```
This Python code defines a function `string_xor` that performs the XOR operation on two input strings. The function takes two string arguments and returns the result as a string. The function is then tested with a series of test cases using the `test_cases` list. The test cases include various combinations of 0s and 1s in the input strings.