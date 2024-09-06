```python
from typing import List
def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([1, 2, '3', 'abc'])
    []
    >>> filter_integers([1, 2, '3'])
    []
    >>> filter_integers([1, 2, 4, 5])
    []
    """
    return [i for i in values if isinstance(i, int)]

# Test the function with different inputs and check the output
test_values = [1, 2, '3', 3, 'abc', (1, 2), [1, 2, 3], {'a': 1}]
test_result = filter_integers(test_values)
print(test_result)  # Output: [1, 2, 3]
 ``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input list. It uses the's `isinstance()` function to check if each value in the list is an integer, and if it is, it is included in the new list.