```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.py  # - list([-1, 2, -4, 5, 6])
test_get_positive.py  # [ [2, 5, 6]
test_get_positive.py # [error]
```

Output should be:
> [2, 5, 6]
> [True]