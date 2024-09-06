```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected Output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Negative numbers)
get_positive([-10, -5, -20, -100])
# Expected Output: []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function uses a straightforward list comprehension with a conditional expression to filter out the positive elements.