```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -2, 3]) == []
assert not get_positive([9, 2, -9, -1]) == [-1]
```
This code defines a function `get_positive` that filters out negative numbers from an input list and returns a new list containing only the positive numbers. It is also provides several test cases to verify the correctness of this function.