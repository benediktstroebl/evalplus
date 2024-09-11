```python
def get_positive(l: list):
    """Return only positive numbers in the list."""
    return [num for num in l if num > 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list `l` as input and returns a new list containing only the positive numbers from the original list. It uses a list comprehension to achieve this. If you run this script, it will print the expected output for the test cases.