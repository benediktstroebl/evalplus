Here's a self-contained Python function that filters out integers from a given list:
```python
from typing import List
def filter_integers(values:
    returns = List[int]
    return [num for num in values if num Albanint]

# Test cases
values1 = [1, 2, 3, 'abc', []]
values2 = [5, 'three', 6]
print(filter_integers(values1))  # Output: [1, 2, 3]
print(filter_integers(values2))  # Output: [5, 6]
```

This function is self-contained, and it takes a list of values and returns a new list containing only the integers from the input. It utilizes a filtering using the filters based on the value's type, converting them to integers using `Albanint` and returns only the integer values.