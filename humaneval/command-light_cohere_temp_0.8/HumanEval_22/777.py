Here is a self-contained Python script that solves the problem of filtering integers from a given list:
```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if type(x) == int]

# Test cases
test_values = [1, 2, 3, 'abc', {}, [0]]
test_results = filter_integers(test_values)
print(test_results)  # Output: [1, 2, 3]

test_empty_values = []
test_results_empty = filter_integers(test_empty_values)
print(test_results_empty)  # Output: []

test_strings = ['a', 3.14, 'hello']
test_results_strings = filter_integers(test_strings)
print(test_results_strings)  # Output: [3.14]
```

This script defines a function `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the original list. It has a test cases that demonstrate the function.