```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if type(x) == int]

# Test cases
test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert len(actual) == len(test_case), f"Test case: {test_case}, actual: {actual}"
```  The function `filter_integers` takes a list of values and returns a new list containing only the integers from the input. This is using list comprehension and the type coercion built-in functions of Python.