```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

values = ['a', 3.14, 5]
print(filter_integers(values))  # Output: [5]

values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Output: [1, 2, 3]

values = [1, 2, 3, 'abc', {}, [0]]
print(filter_integers(values))  # Output: [1, 2, 3, 'abc', [], 0]

values = List([1, 2, 'aa', 3, '123'])
print(filter_integers(values))  # Output: [1, 2, 3]
```
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It uses the specific typing and demonstrates the use of the function with different input scenarios.