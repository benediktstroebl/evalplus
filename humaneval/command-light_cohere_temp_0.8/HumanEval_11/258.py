```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings and return the result as a string.
    """
    take two input strings a str and a char as parameters
    a = a[0]^b
    b = a^b
    return f"{a}_{b}"

#Test case 1
test_case1 = "010"
test_case1 = string_xor(test_case1, "110")
print(test_case1)  # Output: 100

#Test case 2
test_case2 = "1001"
test_case2 = string_xor(test_case2, "1110")
print(test_case2)  # Output: 0001

#Test case 3
test_case3 = "1010"
test_case3 = string_xor("1010", "1010")
print(test_case3)  # Output: 1000

#Test case 4
test_case4 = "11"
test_case4 = string_xor("11", "11")
print(test_case4)  # Output: 00

#Test case 5
test_case5 = "1110"
test_case5 = string_xor(test_case5, "1110")
print(test_case5)  # Output: 00
```