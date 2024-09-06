```python
# Importing required module
from typing import List


# Defining function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Testing the function
# Empty list
test_case_1 = ['']
result_case_1 = concatenate(test_case_1)
print(f"{test_case_1} => {result_case_1}")  # [''] => ''

# List with elements
test_case_2 = ['a', 'b', 'c']
result_case_2 = concatenate(test_case_2)
print(f"{test_case_2} => {result_case_2}")  # ['a', 'b', 'c'] => 'abc'
```

In this script, the `concatenate` function takes a list of strings (`List[str]`) as input and returns a single string. It achieves this by iterating through each element in the list and appending it to a result string. The test cases are also included to verify the function's correctness against different scenarios. 

To run the script, you can either copy the code into a Python file (e.g., `concatenate.py`) or use an online Python interpreter. After running the script, it will output the result of each test case, confirming that the function is working as expected.