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

# Test the function with known good inputs
values_good = [1, 2, 3, 5, 3.5, '14']
print("Good inputs:", values_good)
print("Filter:", filter_integers(values_good))

# Test the function with known bad inputs
values_bad = [1, 2, 3, 'abc', {}, []]
print("\nBad inputs:", values_bad)
print("Filter:", filter_integers(values_bad))
``` 
This script provides a self-contained function filter_integers that filters a given list of any Python values only for integers. The function accepts a list of values and returns a new list with only the integers from the original list. The test cases demonstrate the good and bad inputs with appropriate outputs.