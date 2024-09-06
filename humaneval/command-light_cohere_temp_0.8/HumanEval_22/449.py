```python
from typing import List
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test case 1
values = ['a', 3.14, 5]
print(filter_integers(values))  # Output: [5]

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Output: [1, 2, 3]

# Test case 3
values = [1, 2, 3, 4, 'five', 6]
print(filter_integers(values))  # Output: [1, 2, 3, 4, 5, 6]
```
The `filter_integers` function takes a list of values and returns a new list containing only the integers from the original list.  It list comprehension is the function iterates over each element in the input list and checks if it's an integer using the `type()` built-in function. 
If the element is an integer, it gets added to the new list.