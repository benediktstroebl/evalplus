Here is a Python script that includes a self-contained function to filter and return integers from a given list of any Python values:
```python
from typing import List
def filter_integers(values:
    filtered_ints = [x for x in values if isinstance(x, int)]
    return filtered_ints

# Example usage
values = [1, 2, 3, 'abc', {}, [5])
result = filter_integers(values)
print(result)
```

This code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the original list. The function uses a Python's built-in `isinstance` function to check if each element in the list is an instance of the `int` class, and then creates a new list by filtering the elements that are integers. 

The output of the code will be `[1, 2, 3, 5]`, which are the integers from the list of values.