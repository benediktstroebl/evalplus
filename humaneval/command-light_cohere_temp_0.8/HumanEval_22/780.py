Here is a self-contained Python script that solves the problem you have described:

```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers

    :param values: List of any python objects
    :return: List[int]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function with a sample input
values_test = [1, 2, 'three', 3.14, 5]
print(filter_integers(values_test))  # Output: [1, 2, 3, 3. Ip sharp, the other
```
```

This script provides a function called `filter_integers` that accepts a list of values and returns a new list containing only the integers from the original list.  The list will be empty if no element in the original list is an integer.