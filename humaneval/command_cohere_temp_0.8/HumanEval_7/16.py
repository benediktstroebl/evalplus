```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input list that contain the given substring. This function solves the problem using Python's list comprehension, filtering strings that contain the provided substring. 

To verify the functionality of the function, you can test it with different inputs:
```python
# Test Case 1
input_strings = []  # Empty list
substring = "a"
expected_result = []

result = filter_by_substring(input_strings, substring)
print("Test Case 1 - Input: ", input_strings)
print("Test Case 1 - Expected: ", expected_result)
print("Test Case 1 - Result: ", result)
print("")

# Test Case 2
input_strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
expected_result = ['abc', 'bacd', 'array']

result = filter_by_substring(input_strings, substring)
print("Test Case 2 - Input: ", input_strings)
print("Test Case 2 - Expected: ", expected_result)
print("Test Case 2 - Result: ", result)
```

This will produce the following output:
```
Test Case 1 - Input:  []
Test Case 1 - Expected:  []
Test Case 1 - Result:  []

Test Case 2 - Input:  ['abc', 'bacd', 'cde', 'array']
Test Case 2 - Expected:  ['abc', 'bacd', 'array']
Test Case 2 - Result:  ['abc', 'bacd', 'array']
```

The first test case verifies the function's behavior when the input list is empty, resulting in an empty list. The second test case demonstrates the function's ability to filter strings containing the specified substring ('a' in this case), producing the expected result.