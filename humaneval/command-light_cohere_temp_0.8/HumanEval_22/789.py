Here is a Python script that contains a self-contained function that filters integers from a given list:
```python
from typing import List

# Filtering integers from a list
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],  # Empty list
    ['a', 3.14, 5],  # Non-integer values
    [1, 2, 3, 'abc', {}, []],  # Mixed data types and empty list
    ]

# Function calling and testing
for test_case in test_cases:
    actual_integers = filter_integers(test_case)
    assert all(isinstance(element, int) for element in actual_integers)
    print(f"Test case {test_case}: {actual_integers}")
``` 
This script defines a function called `filter_integers` that filters a list of values to only include integers. 

It provides test cases with various scenarios, including empty lists, non-integer values, mixed data types, and empty lists. The function is then called with each test case, and the output is printed along with the validation of each case.