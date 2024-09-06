```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using only ones and zeros
    """
    return ''.join(c ^ d for c, d in zip(a, b))

# test cases
test_cases = [
    "010",
    "110",
    "00",
    "001",
    "1010",
    "1111",
]

test_results = []

for case in test_cases:
    test_results.append(string_xor(case, case))

for i in range(len(test_results)):
    print(f"{test_cases[i]}: {test_results[i]} == {test_cases[i]^test_results[i]}")

```  This Python code defines a function called **string_xor** that performs the XOR operation on two input strings, consisting only of ones and zeros. It utilizes the zip function to iterate over the two input strings and perform the XOR operation element-by-element on corresponding characters. The function returns the result, also a string.

The code also defines a list of test cases **test_cases**, which includes various strings to test the function. Finally, it performs the loop to iterate over the test cases and compares the output of the **string_xor** function with each case. The results are stored in **test_results**, and finally, it prints out the results of each test case.