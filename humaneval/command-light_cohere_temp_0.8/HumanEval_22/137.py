```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a few cases
values_list = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

print(filter_integers(values_list))  # Expected Output: [5, 1, 2, 3]
```

This function, `filter_integers`, takes a list of values as input and returns a new list containing only the integers from the input list. It uses the use of the list comprehension with the `isinstance` operator to filter out non-integer values from the input list.