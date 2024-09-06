```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with various lists of numbers
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
```

This script defines a function that filters out negative numbers from an input list and returns a new list with only the positive numbers. 

The test suite includes two cases, each testing a different list of numbers.