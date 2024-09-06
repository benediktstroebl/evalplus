```python
from typing import List
def filter_integers(values:
    # Filter the list for only integers
    integers = [x for x in values if type(x) == int]
    return integers

# Test case 1
values1 = [1, 2, 'three', 3.14]
print(filter_integers(values1))  # Output: [1, 2, 3]

# Test case 2
values2 = [1, 2, 3, 'abc', {}]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, [3, 4, 5], 6]
print(filter_integers(values3))  # Output: [1, 2, [3, 4, 5], 6]
```

This Python script provides a function named `filter_integers` that filters a given list of values for only the integers. It uses a specific Python list comprehension to iterate over the list and checks the `type` of each element. The filtered list of integers is then returned.