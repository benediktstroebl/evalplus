Here is a self-contained Python function that filters integers in a list:
```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
test_cases = [
    [],  # Empty list
    ['a'],  # Non-integer
    [1, 2, '3'],  # Mixed integers and non-integers
    [3, 'four'],  # Non-integer value
]

# Function call and tests results
print("Test cases:", test_cases)
print("filtered_integers:", filter_integers(test_cases))

```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses the maint type checking to identify integers and filter them out. The provided test cases cover a following scenarios: empty list, non-integer value, mixed integers and non-integers, and non-integer value.

The output will display the test cases and the corresponding filtered integers.