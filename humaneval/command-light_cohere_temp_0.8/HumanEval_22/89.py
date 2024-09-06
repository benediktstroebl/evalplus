```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([-3, -5, 7, 'hello'])))  # [-3, -5, 7]
```
This script defines a function `filter_integers` that filters a list of values to include only the integers from the list. The function utilizes a list comprehension to iterate through the list of values and checks if each element is an instance of the integer class using the isinstance function. The function returns a filtering process with the list of values. 

The test cases are printed to the console to verify the function.