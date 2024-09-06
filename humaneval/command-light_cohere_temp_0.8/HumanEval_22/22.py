```python
from typing import List
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> ['a', 3.14, 5]
    [5]
    >>> [1, 2, 3, 'abc', {}, []]
    [1, 2, 3]
    """
    return [num for num in values if isinstance(num, int)]

# Test the function
test_values = [1, 2, 3, 'abc', {}, [5]]
result = filter_integers(test_values)
print(result)  # Output: [1, 2, 3]
```
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. 
The provided test values demonstrate that the function successfully filters out non-integer elements and returns the expected output.