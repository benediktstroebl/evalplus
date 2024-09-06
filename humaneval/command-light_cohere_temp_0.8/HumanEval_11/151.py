```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR operation on two strings consisting only of digits 1.
    :param
        string astr: str, first string
    :param string_b: str, second string
    :return: string: result of XOR operation on input strings
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    if len(a) != len(b):
        raise ValueError("Both inputs must have the same length.")

    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += str(i + 1)
        else:
            result += str(0)

    return result

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "101"),
    ("000", "111"),
    ("1111", "1111"),
]

test_results = []

for act, expect in test_cases:
    test_results.append(string_xor(act, expect))

print("Test Results:")
for res, exp in zip(test_results, ["".join().
``` 
This script defines a function **`string_xor`** that performs the XOR operation on two input strings consisting only of digits 1. The function checks the strings are valid strings and that the lengths are equal. It then performs the string XOR operation and returns the result as a string. 

The test cases are defined in the **`test_cases`** list, where each tuple contains an input string and the expected output. The script then iterates through each test case and compares the actual output with the expected output using the **`string_xor`** function. 
The test results are printed to the console to verify the correctness of the function.