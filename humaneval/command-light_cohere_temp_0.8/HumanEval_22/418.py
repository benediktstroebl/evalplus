```python
from typing import List

def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [0]]
print(filter_integers(values))  # Output: [1, 2, 3]

# Another test with list of tuples
values_list = [('a', 3, 'b', (4, 5))]
print(filter_integers(values_list))  # Output: [('a', 3)]
```

This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses the method of list comprehension to filter out the desired elements. 

The script also provides two tests to check the correctness of the `filter_integers` function.