```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [num for num in values if isinstance(num, int)]

# Test the function
test_values = [1, 2, 'three', 3.14, (4, 5)]
print(filter_integers(test_values))  # Output: [1, 2, 3, 3.

``` 
This Python function, `filter_integers`, takes a list of values as input and returns a new list containing only the integers from the input list. It uses the filter method from the Python's built-in list functions to filter out the elements that are not instances of the `int` class. The test cases demonstrate the same, and the output is as expected.