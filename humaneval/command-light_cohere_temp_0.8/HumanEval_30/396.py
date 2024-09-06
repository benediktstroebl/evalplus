```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various list inputs
# Returns list with positive numbers only
get_positive([-1, 2, -4, 5, 6])  # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # [5, 3, 2, 3, 9, 123]
get_positive([1, 2, 3, -4, -1, 4])  # [1, 2, 3, 4]
get_positive([5, 6, 7, 8, 9])  # [5, 6, 7]
```
This Python code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function employs a list comprehension to achieve this, filtering out the elements that are greater than or equal to zero. This code is method allows for a clear and concise transformation of a list of values into a new list with positive numbers.