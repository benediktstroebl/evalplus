```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Output: [1, 2, 3]

# Test case 3
strings_only = ['a', 3.14, 'hello']
print(filter_integers(strings_only))   # Output: []
```

This Python script defines a function named `filter_integers` that filters a list of values and returns a new list containing only the integers. The function uses the filtering logic by iterating through each element in the input list and checking its type using the `isinstance` function. The test cases demonstrate how the **filter_integers** function works by correctly filtering out non-integer elements from the input list.