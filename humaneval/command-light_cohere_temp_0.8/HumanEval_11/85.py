```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ 
    Function to perform XOR operation on two input strings consisting only of digits 1 and 0.
    """
   
    string = a ^ b
    return(f"{a ^ b}")
    """
    return(f"{a ^ b}")

# Test case 1
test_cases = [
    "010",
    "110",
    "0011",
    "000"
]

test_results = []
for tc in test_cases:
    test_results.append(string_xor(tc, "100"))

# Test case 2
test_cases = [
    "0011",
    "0110",
    "000",
    "11"
]

test_results = [test_cases[1:] ^ "0110"],]

# Test case 3
test_cases = [
    "000",
    "0000",
    "000111"
]

test_results = [string_xor("000", "0") ^ string_xor("000111", "00")]

# Print the test results
for tc, result in zip(test_cases, test_results):
    print(f"{tc}: {result}")
 ``` 
The code defines a function called `string_xor` that takes two input strings, a and b, and performs the XOR operation on them, returning the result. The test cases are defined, and the results are printed to the console.