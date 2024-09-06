Here is a Python script with a self-contained function that solves the problem of performing a string XOR operation on two input strings:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of digits '0' and '1'.
    """
    return ''.join(str((a^[i]^b^[i]) for i in range(len(a))))

# Test case 1
test_case_1 = '010'
test_case_2 = '110'
result = string_xor(test_case_1, test_case_2)
print(result)  # Expected Output: 100

# Test case 2
test_case_3 = '0011'
test_case_4 = '1001'
result = string_xor(test_case_3, test_case_4)
print(result)  # Expected Output: 1000

# Test case 3
test_case_5 = '00010001'
test_case_6 = '11'
result = string_xor(test_case_5, test_case_6)
print(result)  # Expected Output: 101
```

The `string_xor` function takes two strings a and b as input and performs a XOR operation on each corresponding character in both strings, it uses the `^` operator to perform the XOR and then converts the result to a string using the `join` method. The function then returns the result, which is also a string. The test cases are passing the results to the print statements and the expected output is shown.