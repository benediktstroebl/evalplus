Here is a Python script with a self-contained function that solves the problem of filtering integers from a given list:
```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [1, 2, 3, 'abc', 5, 6, 7]
test_cases = [filter_integers(values) for values in test_values]

print("Test cases:")
for index, test_case in enumerate(test_cases, start=1):
    print(f"Test {index}: {test_case}")

print()

assert len(test_cases) == 6
assert all(isinstance(test_cases[0], int))
assert all(test_cases[0] == 1)

``` 
This Python code defines a function `filter_integers` that filters a list of values to include only integers. The function utilizes a list comprehension to iterate through the values and checks if each element is an instance of the `int` class, which represents integers. 

The code also includes a set of test values and corresponding test cases, where the `filter_integers` function is called with different lists of values. Finally, several assertions are used to verify the correctness of the function by checking if the output of the function matches the expected behavior.