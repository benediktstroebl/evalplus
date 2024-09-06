Here is a self-contained Python script that defines a function `string_xor` solving the problem you provided: 
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    """
    return ''.join(a ^ b)

# Test case 1
test_case1 = "010"
test_case2 = "110"
print(string_xor(test_case1, test_case2))
# Output should be 100

# Test case 2
test_case3 = "1001"
test_case4 = "1010"
print(string_xor(test_case3, test_case4)))
# Output should be 1010

# Test case 3
test_case5 = "abc"
test_case6 = "123"
print(string_xor(test_case5, test_case6)))
# Output should be 0
 

``` 
This script provides a self-contained function with appropriate input and test cases.