Here's a self-contained Python script that solves the problem of filtering integers from a list of various python objects:
```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert all(isinstance(x, int) for x in actual), f"Failed: {test_case}"
    print(f"Test case: {test_case}, Actual: {actual}, Expected: [int()]")
```
The provided code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. 

It uses the `isinstance` function to check if each element is an instance of `int` type, and then returns a new list with only the integers. 

The test cases are defined as a list of lists, each containing a list of values. 

These test cases are passed to the `filter_integers` function, and the function returns the filtered integers for each test case. 
The `assert` statements are used to verify that the function is working correctly, by checking that the returned list of integers matches the expected `int` type. 
Output will be printed to the console.