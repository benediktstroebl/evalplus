```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, converts it to a set (which automatically removes duplicates), and then converts it back to a list and sorts it before returning the result. The `sorted` function is used to sort the list in ascending order. 

The test case at the end checks that the function behaves as expected by calling it with the example list from the problem statement.