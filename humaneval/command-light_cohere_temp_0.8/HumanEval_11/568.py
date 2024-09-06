Here is a self-contained Python script that solves the problem of performing a XOR operation on two input strings consisting only of ones:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("00100", "01"),
    ("abc", "cba"),
    ("Hello", "olleH"),
    ("", "")
]

# Perform XOR on each test case
for act in test_cases:
    result = string_xor(*act)
    print(result)
```
This code defines a function `string_xor` that performs the XOR operation on two input strings, it takes two strings as input and returns the XOR of these strings. 
The code also includes a list of test cases, which contains a variety of strings that are passed to the function to test its correctness. 

Finally, it iterates over the test cases and performs the XOR operation on each string pair and prints the results.