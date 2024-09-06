```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test case 1: Basic Integer filter
print(filter_integers(['a', 3.14, 5]))  # Output: [5]

# Test case 2: Filter empty list
print(filter_integers([]))  # Output: []

# Test case 3: Filter non-numeric string
print(filter_integers([1, 2, 'abc', {}]))  # Output: [1, 2]

# Test case 4: Filter objects
print(filter_integers([1, 2, 3, 'object']))  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It also comes with several test cases to verify the functionality of the function.