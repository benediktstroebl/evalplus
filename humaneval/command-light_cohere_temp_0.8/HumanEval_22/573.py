```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', (1, 2), [3, 4]}]))  # [1, 2, 3]
```
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. This is using the Python's **isinstance** function to check if each element in the input list is an instance of the **int** class.