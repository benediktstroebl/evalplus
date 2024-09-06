```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Testing the function
values_list = [1, 2, 3, 'abc', 4, 'c', '{"string"}', (5, '6')]
result = filter_integers(values_list)
print(result)  # Output: [1, 2, 3, 4, 'c', 5, 6]
```