```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Example usage:
values_list = [1, 2, 3, 'abc', {}, [1, 2, 3]]
result = filter_integers(values_list)
print(result)  # Output: [1, 2, 3]

# Test with invalid input (non-integer value)
values_list2 = [1, 2, 3, 'four', [], []]
result2 = filter_integers(values_list2)
print(result2)  # Output: []
```
The provided code includes a function called `filter_integers`, which takes a list of values as input and returns a new list containing only the integers from the original input. This is process uses the universal `isinstance` to check if each element is an integer, and if it is, it gets included in the new list. 

It also includes an example usage of the function, where it is called with a list of integers and the output is printed.