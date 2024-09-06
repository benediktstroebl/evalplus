```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [1, 2, 3])
print(filter_integers(values))  # Output: [1, 2, 3]
``` 
This Python function named `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input list. It uses the data type checking to filter out any non-integer values, which is a self-contained solution to the given problem.