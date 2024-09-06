```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
values_list = [1, 2, 3, 'abc', {}, [5]]
result_list = filter_integers(values_list)
print(result_list)  # Output: [1, 2, 3]

``` 
The above script defines a function named `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list.  The uses list comprehension to filter the elements based on their type, and the resulting list is returned. The test case demonstrates that the function successfully filters out the integers from the given list.