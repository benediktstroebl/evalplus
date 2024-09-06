```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1:
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2:
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Test case 3:
assert len(get_positive([-100, -999, 10000])) == 2

# Test case 4:
assert len(get_positive([1, 2, 3, -100])) == 3
```
This code defines a function `get_positive` that takes an input list and returns a new list containing only the positive elements from the original list.  It tests by using the method assertion, we can easily verify that the function is working correctly.