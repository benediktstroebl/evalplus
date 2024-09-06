```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive
test_get_positive([-1, 2, -4, 5, 6])
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```

This script defines a function `get_positive` that takes a list `l` as an argument and returns a new list containing only the positive numbers from `l`. The function uses list comprehension to iterate through the list and filters out the negative numbers using the condition `num >= 0`. The script also provides two test cases to verify if the `get_positive` function is working correctly for different input lists.