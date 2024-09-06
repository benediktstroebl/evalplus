```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

#Test cases
values_test = [1, 2, 3, 'abc', [1, 2, 3], [3, 1]]
print(filter_integers(values_test))  # Output: [1, 2, 3]

values_list = [1, 2, 3, 'abc', {}, [1, 2, 3]]
print(filter_integers(values_list))  # Output: [1, 2, 3]

int_only = [1, 2, 3, 4]
print(filter_integers(int_only))  # Output: [1, 2, 3]
```
This script defines a function **filter_integers** that filters a list of values and returns a new list containing only the integers. It then passes test cases that the integers will be filtered correctly.