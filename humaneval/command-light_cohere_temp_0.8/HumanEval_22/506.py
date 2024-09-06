Here is a self-contained Python script with a function that filters integers from a list:
```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],  # [] -> [] items are always non-integers
    ['a', 3.14],  # filter_integers([1, 2, 3, 'abc', {}, []])  # ['1', '2', '3']
    [1, 2, 3],  # All integers
    'hi', ['len']  # [] and non-int
]

# Function Calls
print(filter_integers(test_cases))  # Output: [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: ['1', '2', '3']
print(filter_integers([1, 2, 3], 'abc'))  # Error: ValueError: 'abc' object is not iterable'
```
This script provides a function filter_integers that takes a list of values and returns a new list containing only the integers. The script also provides a test cases to validate the behavior of the function.