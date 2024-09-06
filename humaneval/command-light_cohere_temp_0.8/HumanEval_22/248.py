```python
from typing import List

def filter_integers(values:
    """ Filters and returns only the integers from the input list"""

    # we use the isinstance to filter out any other than int values
    filtered_ints = [x for x in values if isinstance(x, int)]

    return filtered_ints

# tests
print(filter_integers([3, 'a', 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```
The function uses the `isinstance` function to filter out any values that are not of type `int` from the input list. The output of the filtering is stored in the `filtered_ints` list, and this list is returned by the function.