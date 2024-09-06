```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([10, 2, 'hello', 3]))  # Output: []
``` 
This script defines a function `filter_integers` that takes a list of any Python objects and returns a new list containing only the integers from the input list. 

This function uses the type hint from Python's `typing` module to filter out the integers from the input list, ensuring that it only returns the desired output.