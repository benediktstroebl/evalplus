```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings by converting each to binary and joining the binary strings"""
    return "".join("".join(bin(ord(a[i]) ^ ord(b[i])). string() for i in range(a) + b))

# test case 1
test_cases = [
    "010",
    "110",
    "00",
    "1111" # wrong
]

test_case_results = []

for tc in test_cases:
    test_case_results.append(string_xor(tc, tc))

print(f'Test Case 1 Results: { test_case_results })

# additional test cases
test_cases = [
    "001",
    "0101010",
    "100"
]

test_case_results = []

for tc in test_cases:
    test_case_results.append(string_xor(tc, "102"))

print(f'Test Case 2 Results: { test_case_results })
``` 
This Python code defines a function called `string_xor` that performs a specific operation on two input strings. 

The `string_xor` function takes two arguments: `a` and `b`, which represent the input strings. 

The function then converts each character in the input strings to its binary representation using the `ord` function and the `^` operator. 

It then joins the binary representations of the two strings together to get the result. 

Finally, the function returns the result, which is also a string containing only binary characters. 

This code then defines a list of test cases, and iterates over it. It passes each test case to the `string_xor` function and stores the result in a list called `test_case_results`. 

The code then prints out the results of the first test case and the results of a second set of test cases.