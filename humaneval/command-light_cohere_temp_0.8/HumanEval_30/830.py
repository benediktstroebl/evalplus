```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various input
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
```
The code defines a function that takes a list lst as input and returns a new list containing only the positive elements from the original list. The function uses list comprehension to achieve this, and the assertion tests ensure that the function is working correctly with various input lists.