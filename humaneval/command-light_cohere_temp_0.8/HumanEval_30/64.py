```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
```
This code defines a function `get_positive` that takes a list and returns a new list with only the positive elements from the original list. The code also includes two test cases to ensure the correctness of the `get_positive` function.