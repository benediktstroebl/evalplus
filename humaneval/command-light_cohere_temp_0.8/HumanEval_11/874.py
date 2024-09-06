```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a string.
    """
   
    XOR = lambda x, y: x ^ y
    # Compare with built-in xor
    return ''.join(XOR(a, b)))

# Test case 1
test_cases = [
    "010".join(),  # 010
    "001".join(),  # 0^1
    "100".join(),  # 100
    "110".join(),  # 10^1
    "000".join(),  # 00^0
    "0000"
]

# Test case 2
test_cases2 = [
    "0000",
    "10010",
    "01001",
    "00010",
    "00011"
]

def run_tests():
    """
    for test_case in test_cases:
        print(f"Test case: {{test_case})")
        print(string_xor(test_case, test_case))
        print("\n")

    for test_case in test_cases2:
        print(f"Test case: {{test_case})")
        print(string_xor(test_case, test_case))
        print("\n")

run_tests()
``` 
This Python script defines a function `string_xor` that performs a binary XOR operation on two input strings, which contain only the characters '1' and '0'. The function then returns the result of the XOR operation as a string.

The script also includes two test cases: `test_cases` and `test_cases2`. For each test case, the script prints the input string and the expected output string, then calls the `string_xor` function with the corresponding input strings. 

Finally, the `run_tests` function is called to execute the test cases.