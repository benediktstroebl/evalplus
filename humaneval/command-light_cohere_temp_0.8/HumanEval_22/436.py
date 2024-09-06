```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
result = filter_integers(values)
print(result)  # Output: [5, 1, 2, 3]

# Test with other data types
result_bool = filter_integers([1, 2, 3, 'abc'])
print(result_bool)  # Output: []

result_str = filter_integers(['a', 'bc'])
print(result_str)  # Output: ['a', 'bc']
```  This script defines a function **filter_integers** that filters a list of values for only the integers. It then passes these function with a few test cases and displays the results.