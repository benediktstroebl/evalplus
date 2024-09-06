```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    [],
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

results = filter_integers(test_filter_integers)

for case, expected in zip(test_filter_integers, results):
    print(f"Case: {case} == Expected: {expected} => {results[case]}")
```  This code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the`is watched` approach to filter out non-integer elements from the list.