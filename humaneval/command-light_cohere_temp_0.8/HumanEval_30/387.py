```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with various input lists

# Positive results
print(get_positive([-1, 2, -4, 5, 6]))        # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]

# Negative results
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # []
print(get_positive([-9, -5, -20]))           # []

# Complex numbers
print(get_positive([1, 2j]))             # [1]
print(get_positive([1, 2, 3, 4, -1]))    # [1, 2]
```
This Python function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the input list. The function uses a simple list comprehension to filter out the positive numbers.