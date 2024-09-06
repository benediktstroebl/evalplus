```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1: Get positive numbers from a list
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2: Get positive numbers from a list of mixed values
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
The above Python code defines a function called `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The function uses list comprehension and the statement `if num >= 0` to filter out only the positive numbers from the list.