```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases for function
values_test = [1, 2, 3, 'abc', {}, [0, None, []]]
print(filter_integers(values_test))  # Output: [1, 2, 3]
```
This Python code defines a function called **filter_integers** that filters a list of values based on whether each element is an integer. The function uses a list comprehension to achieve this. It then passes the value tests to this function and prints the resulting filtered list. The test case ensures the filter function works correctly for a variety of data types.