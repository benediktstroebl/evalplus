```python
from typing import List
def filter_integers(values:
    """ Filters and returns only the integers from the input list"""
    filtered_ints = [x for x in values if isinstance(x, int)]
    return filtered_ints

#Test case 1
test_values = ['a', 3.14, 5]
filtered_ints = filter_integers(test_values)
print("Test case 1: Result =", filtered_ints)

#Test case 2
test_data = [1, 2, 3, 'abc', {}, []]
filtered_ints = filter_integers(test_data)
print("Test case 2: Result =", filtered_ints)
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a filtering technique to identify and return the integers in the list.

The script also includes two test cases, passing different lists of values to the `filter_integers` function, and the output is printed to the console.