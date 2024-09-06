```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists
print(get_positive([-1, 2, -4, 5, 6]))   # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123]
```
This function, `get_positive()`, uses list comprehension to filter out negative numbers and returns a new list containing only the positive numbers. This script is essential for solving the problem of getting positive numbers out of a given list.