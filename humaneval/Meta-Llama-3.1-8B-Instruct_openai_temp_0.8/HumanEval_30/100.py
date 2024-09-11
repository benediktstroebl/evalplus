### Solution
```python
def get_positive(l: list):
    """Return only positive numbers in the list."""
    return [num for num in l if num > 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # Expected: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to filter out negative numbers from the input list. It iterates over each number `num` in the list `l` and includes it in the result list if `num > 0`.